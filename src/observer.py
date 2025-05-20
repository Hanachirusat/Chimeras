import time
import weakref

#当前的版本监控所有属性，一旦属性发生变化就通知所有的队友。
class ObservableMeta(type):
    """元类用于自动创建属性观察逻辑"""
    def __new__(cls, name, bases, dct):
        # 自动为标记的属性创建观察逻辑
        if '__observed_attrs__' in dct:
            attrs = dct['__observed_attrs__']
            for attr in attrs:
                # 为每个被观察属性生成属性描述符
                private_attr = f"_{name}__{attr}"

                #下面的操作相当于对继承该元类的类的私有属性设置@property
                def getter(self, name=private_attr):
                    return getattr(self, name)

                def setter(self, value, name=private_attr, attr=attr):
                    old_value = getattr(self, name)
                    if old_value != value:
                        setattr(self, name, value)
                        #修改属性的时候，调用类的notify_observers方法
                        # 通知所有的观察者属性发生了变化
                        self.notify_observers(attr, old_value, value)
                dct[attr] = property(getter, setter)
        return super().__new__(cls, name, bases, dct)


class ChimerasEntity(metaclass=ObservableMeta):
    """所有可观察对象的基类"""
    __observed_attrs__ = ()  # 需要子类指定要观察的属性

    def __init__(self, name):
        self.name = name
        self._observers = weakref.WeakSet()
        self.queue = None  # 所属队列的弱引用

    def add_observer(self, observer):
        if not isinstance(observer, ChimerasEntity):
            raise TypeError("观察者必须是ObservedEntity类型")
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.discard(observer)


    #该方法在setter的时候被自动调用，get和set是所做的特殊操作由元类来实现
    def notify_observers(self, changed_attr, old_value, new_value):
        for observer in self._observers:
            observer.eval(self, changed_attr, old_value, new_value)

    def eval(self, changed_obj, changed_attr, old_value, new_value):
        #打印检测信息
        print(f"[类名：{self.__class__.__name__}，实例名：{self.name}] 检测到变化："
              f"【{changed_obj.__class__.__name__}】{changed_obj.name} 的"
              f"{changed_attr} 属性从 {old_value} 变为 {new_value}")

    def __del__(self):
        # print(f"执行{self.__class__.__name__}的析构函数")
        queue_ = getattr(self, 'queue', None)
        if queue_ is not None:
            # print("从队列中删除")
            queue_.remove_member(self)
            self.queue=None


class Task():
    def __init__(self,atk=5,hp=150):
        self._atk = atk
        self._hp = hp

    @property
    def atk(self):
        return self._atk
    @atk.setter
    def atk(self,value):
        self._atk=value

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,value):
        self._hp=value
class InteractionQueue:
    """管理相互观察的队列"""
    #1 观察所有 2
    #2 观察除了自己外的所有 1
    #3 只观察自己 0
    def __init__(self):
        self.members_list =[]
        self.leader=None
        self.work=None
        self.episode=0
    def add_member(self, member):
        if not isinstance(member, ChimerasEntity):
            raise TypeError("成员必须是ObservedEntity类型")

        # 建立新成员和已有成员的相互观察关系。

        # 判断新成员是否观察已有成员
        if member.mode>0:
            for existing_member in self.members_list:
                #观察其他所有成员，所有要把当前成员添加到其他所有成员的观察者列表中
                existing_member.add_observer(member)
                #如果其他的成员的moce>0则表示其他成员要观察新成员，即新成员的观察者列表中要添加已有的成员
        #2和0 判断新成员是否观察自身
        if member.mode%2==0:
            # 观察自己和加入队列
            member.add_observer(member)  # 观察自己

        # 判断已有成员是否观察新成员
        for existing_member in self.members_list:
            if existing_member.mode > 0:
                member.add_observer(existing_member)

        self.members_list.append(member)
        member.queue = self
    def remove_member(self, member):
        """安全移除成员并清理观察关系"""
        if member not in self.members_list:
            return

        # 清理双向观察关系,
        # current_member队列中包含所有成员，即包含member
        for existing_member in self.members_list:
            # 其他成员不再观察被移除者
            existing_member.remove_observer(member)
            # 被移除者不再观察其他成员
            member.remove_observer(existing_member)
        member.queue = None  # 清除队列引用
        # # 移除自我观察
        # member.remove_observer(member)
        # 从队列中移除
        self.members_list.remove(member)
    def clear(self):
        """清空整个队列"""
        for member in list(self.members_list):
            self.remove_member(member)


        # # 新成员观察所有现有成员
        # for existing_member in self.members:
        #     member.add_observer(existing_member)
    def add_leader(self,leader):
        if not isinstance(leader, ChimerasEntity):
            raise TypeError("成员必须是ObservedEntity类型")

        # 建立新成员和已有成员的相互观察关系。

        # 判断新成员是否观察已有成员
        if leader.mode>0:
            for existing_member in self.members_list:
                #观察其他所有成员，所有要把当前成员添加到其他所有成员的观察者列表中
                existing_member.add_observer(leader)

        #2和0 判断新成员是否观察自身
        if leader.mode%2==0:
            # 观察自己和加入队列
            leader.add_observer(leader)  # 观察自己
        self.leader=leader
        leader.queue = self

    def remove_leader(self,leader):
        """安全移除成员并清理观察关系"""
        if self.leader!=leader:
            print("领队不在当前队列中")
            return
        for existing_member in self.members_list:
            # 删除领队的观察者身份（清空队列中其他成员的观察者弱引用）
            existing_member.remove_observer(leader)
        leader.queue = None  # 清除队列引用
        # 清空自身观察，因为自身不在member_list中
        leader.remove_observer(leader)
        # 从队列中移除
        self.leader=None

    #工作一次
    def work_once(self):
        before_work_hp=self.work.hp
        work_chi=None
        for chi in reversed(self.members_list):
            if chi.hp>0 and chi.on:
                work_chi=chi
                break
        #开始工作，这时进触发自己hp降低的被动
        self.work.hp-=work_chi.atk
        after_work_hp=self.work.hp

        #开始触发技能，自身 体力降低,或同伴累倒后
        work_chi.hp-=self.work.atk
        #触发工作时和完成工作时的被动
        work_chi.work_num+=1
        if before_work_hp>0 and after_work_hp<1:
            work_chi.complete_work_num+=1

    #一回合的工作
    def work_episode(self):
        self.episode += 1
        print(f"===开始第{self.episode}回合的工作===")
        #先处理episode+1的逻辑，这时可能会触发被动，这个被动可能加攻击力
        for chi in self.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
        print("\t工作前：")
        print("\t", end="")
        for chi in self.members_list:
            print(f"{chi.name}[atk:{chi.atk},hp:{chi.hp}]", end="")
        print("\n",end="")
        print(f"\tWork[atk:{self.work.atk},hp:{self.work.hp}]")
        # 奇美拉开始工作
        self.work_once()
        print("\t请脑部工作画面呀QwQ")
        # 根据奇美拉的生命值判断是否应该离场，并触发离场被动
        for chi in self.members_list:
            if chi.hp<1:
                chi.on=False
                self.remove_member(chi)
            #防御性编程
            if chi.on==False:
                self.remove_member(chi)
        print("\t工作后：")
        print("\t", end="")
        for chi in self.members_list:
            print(f"{chi.name}[atk:{chi.atk},hp:{chi.hp}]", end="")
        print("\n",end="")
        print(f"\tWork[atk:{self.work.atk},hp:{self.work.hp}]")
        #如果本回合结束后奇美拉都离场了
        if len(self.members_list)==0:
            return False
        else:
            return True

    #开始工作 
    def begin_work(self,work):
        self.work=work
        print("开始工作...")
        #奇美拉登场
        for i in self.members_list:
            i.on=True

        self.leader.on=True
        #1 更新回合数，固定攻击力
        #2 第一个奇美拉攻击（立即判断工作是否被完成）
        #3 其他奇美拉发动技能）
        #4 判断奇美拉是否离场（循环内判断），或者工作是否被完成（循环条件判断）
        while(work.hp>0):
            live=self.work_episode()
            if not live and work.hp>0:
                print("工作未完成，奇美拉都累坏了~")
        print("工作已全部完成~")


