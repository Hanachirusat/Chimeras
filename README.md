# 奇美拉项目

>**任务队列：**任务队列是一系列待完成的任务的有序组合。每个任务都有一定的生命值和攻击力。
>
>**奇美拉：**每个奇美拉都有一定的生命值和攻击力，部分奇美拉有特殊的被动技能。
>
>**工作：**奇美拉选定一个任务，每次工作使得该任务的生命值降低（降低程度等于奇美拉的攻击力），并且该奇美拉的生命也会降低（降低程度等于任务的攻击力）。当任务的攻击力为0时，任务被完成，当奇美拉的生命值为0时，奇美拉会离场。
>
>**对头奇美拉：**玩家可以选择多个奇美拉组成一个有序的奇美拉队列，当奇美拉离场时，按照顺序使得下一个奇美拉成为队头奇美拉。
>
>**可选定任务：**在任务队列中，只有队头任务可以被选中，当队头任务被完成后，按照顺序使得下一个任务成为队头任务。
>
>**游戏规则：**对局开始前，玩家可以选择多个**奇美拉**去完成**任务队列**里的任务。游戏开始后，在每个回合只有**队头奇美拉**可以选定任务队列里的**可选定任务**开始**工作**。领队奇美拉位于后台，不参与工作，会根据自己的能力给其他奇美拉添加增益效果。当任务队列中的所有任务均被完成时，游戏结束即，玩家取得胜利；当所有奇美拉（领队奇美拉除外）均离场时，游戏失败。

## 奇美拉(Chimeras)档案

###   领队

**职业经理【自我驱动】：**==登场后==：使全体奇美拉`效率+3`，`体力+3`

**严酷恶魔【不准停！】：**奇美拉==完成工作后==，使其`效率+5`

**职场清流【抚慰之心】：**==登场后==：全体奇美拉`效率+2`。奇美==拉追加工作==后：使其`效率+1`

###   成员

**摸鱼仔【3,2】**：平平无奇

**负能量【7，3】：**平平无奇

**真老实【1，16】：**平平无奇

**小坏蛋【3，5】：**平平无奇

**压力怪【5，3】**：平平无奇

**治愈师【温暖，2，5】：**==每回合开始==，使前一格同伴`体力+1`

**小团体【排外，3，3】：** ==每回合开始时==，使前两格同伴`效率+1`，其余同伴`体力-1`

**画饼王【话术，2，7】：**==登场后==所有同伴`效率+8 `,==若自身在场，每回合==使所有同伴`效率-2`

**平凡王【联合，7，7】：**==登场后==，获得场上`所有无特性同伴100%的效率和体力`（单次上限均为25）

**坏脾气【发作，AT:2，HP:9】：**==自身工作时==：使`后一格`同伴`体力-1`

**抗压包【熟练，2，5】：**==自身体力降低时==使`前后一格`同伴`效率+1`



**请假狂【装病，2，7】：**==自身体力降低后==，与`后一格`同伴`交换位置`，并使自身`效率+2`   

**请假王【开摆，6，3】**：==自身体力降低后==，与`后一格`同伴`交换位置`，并使自身`体力+3`

**内卷王【激励，3，8】：**==自身完成工作时==：获得`效率+2`，`体力+3`  【hp<0也会生效，在每回合结束后才让hp<0的奇美拉退场。】

**受气包【道歉，2，5】：** ==自身体力降低时==，使全局同伴`效率+1`

**小夸夸【鼓励，3，3】：**==同伴工作或追加工作时==，若同伴效率》5使其`效率+2 `



**跑路侠【怂恿，1，1】**：==自身累倒时==，和后一格同伴一起`逃离工作`，并使其他同伴`体力+8`



**看乐子【围观，3，3】**：==同伴累到后==，自身`效率+2`，`体力+2`

**背锅侠【接锅，3 ，6：**==同伴累倒时==，使该同伴`体力+10`，自身逃离工作

**抢功劳【，15，2】：** ==同伴工作时==：若自身效率》=剩余工作进度，则进行`追加工作`完成该任务

**急先锋【带头，2，5】：**==同伴工作或追加工作时==，自身与前一格同伴`交换位置`，并且`体力+6`

**说怪话【暗讽，14，1】：**==同伴完成工作时==，使该同伴`效率+4 `并发表自己的意见 

**帮倒忙【捣乱，-1，5】：**==同伴工作时==，自身进行一次`追加工作`

**工作狂【争先 6，10】：**==同伴工作或追加工作时==，进行一次等于自身50%效率的`追加工作`





##  奇美拉被动技能

奇美拉的技能可以抽象为一种形式：满足条件，触发技能。因此我们可以非常自然的采用观察者模式来实现被动技能方法的自动调用。奇美拉行动后，如果某个条件得到满足，则通知该奇美拉的所有观察者。由于每个奇美拉行动后都有可能使得某个可以触发其他奇美拉被动技能的条件得到满足，因此每个奇美拉是subject，也是observer，这是一个==多对多==的观察关系。

通过对奇美拉的技能触发条件进行分析，我们可以把技能分成两类：自身触发和队友触发。自身触发条件中包含生命值降低这种属性（变化）触发，也包含同伴工作或追加工作这种动作触发，此外还有登场技能和回合技。队友触发条件同理。因此从代码实现层面，技能触发可以分为属性触发和动作触发。

属性触发很简单，如果奇美拉的属性发生了变化，则同时他的所有观察者，由观察者判断该属性的变化是否会触发自身的技能。而动作触发反映在代码层面可能是奇美拉执行完某个方法后，通知他所有的观察者。人都是喜欢偷懒的，那么有没有把所有触发条件统一起来的方法呢？

答案显而易见，我们可以把动作触发转变为属性触发，例如同伴工作时触发的技能，我们可以对奇美拉增加一个属性：工作次数，当奇美拉工作后，该工作次数+1。这样就可以把工作触发（动作触发）转变为属性触发。同时我们把工作逻辑剥离出来（后续将解释为什么），把每个奇美拉抽象为一个只有被动技能方法（用eval表示）的类（最终实现版本还是有其他方法的，在后面我们将一一介绍why，what以及how），并且该被动技能是自动触发的。

最后，我们继续简化，不同奇美拉的技能触发条件不同，这是不是意味着观察者模式的实现很复杂？实则不然，我们可以让奇美拉监控所有的属性，然后在eval方法中判断变化的属性是否符合奇美拉技能触发的条件。

##  多对多观察者关系实现

基于上一小结的介绍，在本小节，我们将详细描述如何利用元类来实现多对多的观察者关系。

由于我们把所有的触发条件都转换为了属性触发，那么当奇美拉的任意属性（可能触发其他奇美拉被动的属性）发生变化时，都应该通知观察该奇美拉的观察者。换句话说，我们需要控制每个属性的set过程。自然而然的方法就是property装饰器。我们在元类中遍历所有的属性，处理这些属性get和set时的逻辑。即set时将通知所有的观察者，属性发生了变化。

```python
class ObservableMeta(type):
    """元类用于自动创建属性观察逻辑"""
    def __new__(cls, name, bases, dct):
        # 自动为可能触发其他奇美拉技能的属性创建观察逻辑
        if '__observed_attrs__' in dct:
            attrs = dct['__observed_attrs__']
            for attr in attrs:
                # 为每个被观察属性生成属性描述符
                private_attr = f"_{name}__{attr}"

                #下面的操作相当于对继承该元类的类的私有属性设置@property和@attr.setter(
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
```

在上述代码中，由于我们把奇美拉的属性定义为了私有属性，因此我们需要修改访问私有属性的形式`private_attr = f"_{name}__{attr}"`其中attr是私有属性，private_attr是可以直接访问私有属性的形式（注：python中没有真正意义上的私有属性，私有属性只不过实际换了个名字存储而已，有兴趣的可以详细了解下）。我们在修改属性值的时候，会记录变化的属性，旧值和新值。然后把这些值传递给观察者。

接下来我们实现所有奇美拉的基类，在该基类中我们定义了增加和移除观察者的方法，通知观察者的方法以及析构函数

```python
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
```

在上述代码中，我们保存所有观察者的弱引用，这个弱引用是一个集合的形式，无法保证顺序。这可能就是本项目为什么和实际游戏中奇美拉的行动顺序不一致的原因（==注意：只是行动顺序不一致，每回合的结果是一致的！后面我们会讲为什么==）。基类中的queue属性表示的是奇美拉所属的队列（队列的含义详细请参考上一篇博文：[游戏开发实战（一）：Python复刻「崩坏星穹铁道」嗷呜嗷呜事务所---源码级解析该小游戏背后的算法与设计模式【纯原创】-CSDN博客](https://blog.csdn.net/coreyckw/article/details/148074894?spm=1001.2014.3001.5501)，队列的实现我将在后面详细介绍）

在上述代码中eval方法打印的是辅助判断的信息，实际每个奇美拉都会有自己的eval方法（继承重写该方法）。由于后面我们在奇美拉队列类（InteractionQueue）中保存的是所有奇美拉的强引用，因此该析构函数当且仅当该奇美拉已经从队列中移除后才会调用。如果奇美拉队列还保留着当前奇美拉对象的引用，直接del奇美拉对象，python解释器并不会立刻执行该奇美拉对象的析构函数之后销毁该对象。

也就是说，我们最终还是需要手动调用奇美拉队列类的方法，把当前奇美拉对象从队列中移除。我们在析构函数中所做的操作似乎是多余的！是的至少目前为止是多余的，该析构函数的执行只有当该析构函数中的操作都做了之后才会执行。为什么还要这么写？

这是因为我们后续优化的时候需要把queue中的强引用列表和奇美拉基类中的弱引用集合都变为有序弱引用。优化后析构函数中的操作相当于一层保险，如果没有主动调用奇美拉队列中的移除方法，也不会造成内存泄漏（因为奇美拉队列中是弱引用，并不会增加引用计数，del奇美拉对象的时候会正常执行奇美拉对象的析构函数从而从队列中移除该奇美拉）。同时用有序弱引用也可以调整奇美拉行动顺序从而和游戏中的顺序保持一致。

##  管理奇美拉的队列

我们用一个奇美拉队列来维护当前奇美拉队列，处理不同奇美拉的观察逻辑。当每一个奇美拉入队的时候，根据奇美拉技能触发类型（自身触发还是队友触发），构建这些奇美拉的观察者序列。奇美拉队列中记录了奇美拉在队伍中共的顺序，奇美拉领队和待完成的工作。

1.  添加成员方法中将根据当前成员的观察模式（也就是技能触发的类型，观察模式为2代表观察所有包括自己，1代表进观察同伴，0代表仅观察自身），对不同的奇美拉对象添加管擦或者。注意处理完当前待添加的奇美拉对象后，还要处理已有奇美拉对象。
2.  移除队列方法遍历当前所有奇美拉对象，并移除双向观察逻辑。
3.  清空队列方法，调用移除队列方法清空对象。
4.  添加和删除领队和添加和删除奇美拉对象类似。

```python
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
        #2和0 判断新成员是否观察自身
        if member.mode%2==0:
            # 观察自己和加入队列
            member.add_observer(member)  # 观察自己
		#如果其他的成员的mode>0则表示其他成员要观察新成员，即新成员的观察者列表中要添加已有的成员
        for existing_member in self.members_list:
            if existing_member.mode > 0:
                member.add_observer(existing_member)

        self.members_list.append(member)
        #我们在每个奇美拉对象中记录所在队列的对象，方便后续的技能处理逻辑的实现。
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
```

在上述奇美拉队列类中，我们把领队和工作奇美拉分开管理，方便后续奇美拉技能导致的队列变动。

用一个类对象来管理奇美拉对象有很多好处，刚开始没考虑到的事情后面可以直接添加到奇美拉队列类中，比如抢功劳奇美拉中需要判断当前工作的进度，而在奇美拉对象中共无法直接获得工作进度。可以选择修改eval函数的接口，修改eval函数的接口就要修改基类的接口，导致需要修改其他已实现的代码。因此我最后选择直接在奇美拉队列类中新增一个属性，保存当前待完成的工作，因为每个奇美拉都保留了当前队列的引用，可以直接获得当前工作的进度。

**扩展：**用奇美拉队列类来管理工作队列，开始时我们创建奇美拉对象然后添加到奇美拉队列对象中，注意添加顺序，最左面的奇美拉应该先添加。最后当任务完成后，我们需要调用奇美拉队列对象的移除方法移除所有的奇美拉对象，然后del所有的奇美拉对象。对象删除之类的操作在实际生产环境中是非常重要的。而在本项目中，所有奇美拉对象在主程序执行完毕后销毁。

##  规则定义

这里的很多规则是在实现过程中不断完善的，有了方便读者阅读和理解，在此我先给出所有的规则，之后再给出所有奇美拉类的具体实现。

-   **工作相关：**采用回合制，第一回合开始的时候统一设置奇美拉登场相关的属性从而触发奇美拉登场技能。后续的每回合都做如下操作：

    1.  每回合开始时回合数加1，以便触发奇美拉每回合的技能。
    2.  固定奇美拉攻击力，这点非常重要！！这保证了本项目的结果和游戏结果一致！！因为在实际游戏中，对于攻击力的buff最后才会执行，因此我们固定攻击力快照后，即使增加攻击力的buff（增加攻击力的buff影响的是攻击力本身，并不影响攻击力快照）提前执行，也并不影响实际的结果！！！
    3.  第一个奇美拉工作。工作逻辑为先处理工作对象的hp，再处理当前对象的hp，判断当前工作是否已经被完成，工作数量+1。先判断工作是否被完成，再工作数+1是正确绑定工作完成关系的关键。因为当前奇美拉已经完成工作，并且先工作+1，那可能会触发其他奇美拉的追加攻击，导致程序判定触发被动的奇美拉完成工作。（这涉及到后面的规则，为了和游戏结果保持一致，工作已经被完成也会继续追加攻击以便继续加buff）。
    4.  判断奇美拉hp是否小于1，如果小于1则离场。如果奇美拉的hp小于1并且代表登场的属性为False，则奇美拉也离场（其他奇美拉的技能可能会导致奇美拉hp>0但是直接离场）

-   **奇美拉相关**

    1.  工作已经被完成也会继续追加攻击以便继续加buff

    2.  奇美拉如果导致其他奇美拉直接离场，并不会修改离场奇美拉的hp，也不会从队列中移除该奇美拉，而是修改该奇美拉对象中表示登场的属性为False

        这么做可能会出现一个问题，那就是游戏中奇美拉离场的动作优先级很高，而在本项目实现中，奇美拉离场逻辑在每回合最后才处理。这可能导致奇美拉离场和交换位置相关技能之间的联动和游戏中的结果不一致。因此在本项目中，我们做出一致性规定：奇美拉一定在本回合工作结束，所有技能都触发后才离场。交换位置的技能发动后，奇美拉可以和将要离场但是还未离场的奇美拉交换位置。

        做出如上规定后，与交换位置相关的技能的代码逻辑就变得简单多了，我们只需要考虑当前位置即可，不需要考虑当前位置前后的奇美拉是否已经离场。

    3.  奇美拉技能发动的大前提一定是奇美拉在场！！这点和上面的2有联动。

    4.  工作已经被完成后，奇美拉会继续追加攻击当前被完成的工作，以便吃到buff加成。

    5.  奇美拉技能执行期间，如果可能触发其他技能，那应该保证当前需要处理的逻辑处理完成后再修改可能触发技能的属性。由于这种情况很少，因此我用这种简单的方法保证”原子性“（这么说并不准确！！只是方便理解把）。比如如果奇美拉追加攻击后，应该先判断工作是否被完成再增加奇美拉追加工作的次数。因为增加追加工作次数可能触发其他奇美拉的被动（同伴工作或者追加工作触发的被动）

    6.  奇美拉体力降低到0时不会立刻退场，等到回合结束后统一离场=其他奇美拉技能可以增加hp）。==同伴累到的判断条件为奇美拉的hp小于0。因此可能会出现这么一种情况，同伴累到时的触发的被动可能会被同一个奇美拉触发多次，这点是否在游戏中也是如此本人并没有验证，在此指出==）

    7.  在eval中，如果我们操作可能被监控的属性，应该用非下划线的形式，否则不会被监控到。在本项目中，只要属性变化一定会调用观察者的eval，因此我们需要准确处理eval中的逻辑，如果不满足条件应该提前推出eval函数。（==在最后的优化讨论中，我将给出优化方向，奇美拉仅监控其他奇美拉会触发技能的属性，而不是监控所有属性==）

    8.  技能对同伴的操作一律不包含自身，例如使得同伴体力全部+8，不包括自身。我并没有验证游戏结果，而是仅从字面意思判断，同伴肯定指的是自己之外的奇美拉。我自己是这么理解的，如果游戏中同伴也包括自身，则对应修改即可，本项目则坚持同伴指的是自己之外的奇美拉。

##   奇美拉属性

```python
self.name=name  #奇美拉名字
self.__atk=1  
self.__hp=1
self.__episode=0  #回合数，用于触发回合技
self.__on=False  #是否在场，True为登场，刚开始的时候为False
self.__work_num=0  #工作次数，用于触发 【同伴工作后】的技能
self.__append_work_num=0  #追加攻击次数，用于触发 【同伴追加工作后】的技能
self.__mode=0  #监控规则，详情见正文描述
self.__skill=True  #奇美拉是否有技能
self.__complete_work_num = 0  #奇美拉完成工作次数，用于触发【同伴完成工作】的技能
self.__fixed_atk=0  #每回合开始奇美拉的攻击快照。保证了本项目结果和游戏结果的一致性。
```



##  奇美拉类

###  摸鱼仔，负能量，真老实，小坏蛋，压力怪

这些奇美拉并没有技能，平平无奇。我们对所有奇美拉的攻击力快照设置了property（只读）。我们不希望可以随意更改奇美拉快照，而只有每回合开始时调用相应的方法来固定攻击力快照。

```python
#**摸鱼仔【3,2】**：平平无奇
class Myz(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=2
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #观察模式，2观察所有1观察自身外的所有0只观察自身
        self.__skill=False
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        pass

#**负能量【7，3】：**平平无奇
class Fnl(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=7
        self.__hp=3
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0
        self.__skill=False
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        pass

#**真老实【1，16】：**平平无奇
class Zls(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=1
        self.__hp=16
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0
        self.__skill=False
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        pass

#**小坏蛋【3，5】：**平平无奇
class Xhd(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=5
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0
        self.__skill=False
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        pass

##**压力怪【5，3】**：平平无奇
class Ylg(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=5
        self.__hp=3
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0
        self.__skill=False
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        pass
```

###  治愈师

==每回合开始==，使前一格同伴`体力+1`

治愈师进观察自身，如果变化的属性不是自己则直接返回。代码中的`new_value-old_value)==1`是防御性编程。用于辅助发现episode相关的逻辑错误（每回合episode只能+1）

```python
#**治愈师【温暖，2，5】：**==每回合开始==，使前一格同伴`体力+1`
class Zys(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=5
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        if changed_attr=="episode" and (new_value-old_value)==1 and self.__on:
            position=self.queue.members_list.index(self)+1
            #如果前面一格有队友
            if position<=len(self.queue.members_list-1):
                self.queue.members_list[position].hp+=1
```

###  小团体

==每回合开始时==，使前两格同伴`效率+1`，其余同伴`体力-1`

小团体的实际技能生效情况和自身位置相关。我们先对它前面两格（直到队头奇美拉）的同伴效率+1。其余体力同伴-1可能会触发其他奇美拉的被动技能，因此我们先记住其余奇美拉对象，然后再对这些奇美拉对象的hp-1。

```python
class Xtt(ChimerasEntity):
    #
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=3
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否登场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        if changed_attr=="episode" and (new_value-old_value)==1 and self.__on:
            position=self.queue.members_list.index(self)
            l=len(self.queue.members_list)
            #前两格同伴效率+1
            for i in range(position+1,min(position+3,l)):
                self.queue.members_list[i].atk += 1
            # 其余同伴体力-1，体力-1可能触发其他同伴的技能导致位置发生变化
            # w我们先记录需要-1的同伴
            chi_hp_decrease=[]
            for i in range(position):
                chi_hp_decrease.append(self.queue.members_list[i])
            for chi in chi_hp_decrease:
                chi.hp -= 1
```



###  画饼王

登场技判断需要保证旧值为False。回合技能需要保证再第二回合触发。

```python
# **画饼王【话术，2，7】：**==登场后==所有同伴`效率+8 `,==若自身在场，每回合==使所有同伴`效率-2`
class Hbw(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=7
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #登场后，所有同伴效率+8
        if changed_attr=="on" and old_value==False and self.__on:
            for i in self.queue.members_list:
                if i!=self:
                    i.atk+=8
        # 若自身在场，每回合所有同伴效率-2，这个应该从第二回合开始算,第二回合的时候1-》2.old_value应该为1
        if changed_attr=="episode" and (new_value-old_value)==1 and old_value>0 and self.__on:
            for i in self.queue.members_list:
                if i!=self:
                    i.atk-=2
```



###  平凡王

先记录场上所有无特性同伴的效率和体力，之后进行截断（上限为25）。==注意：这里单词的实际意思可能是单个奇美拉的意思，因为登场技能只会发动一次，因此不存在技能发动单次的含义==）

```python
# **平凡王【联合，7，7】：**==登场后==，获得场上`所有无特性同伴100%的效率和体力`（单次上限均为25）
class Pfw(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=7
        self.__hp=7
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #登场后，获得场上所有无特性同伴100%的效率和体力
        if changed_attr=="on" and old_value==False and self.__on:
            a,h=0,0
            for i in self.queue.members_list:
                if i!=self:
                    a+=min(i.atk,25)
                    h+=min(i.hp,25)
            #单次上限均为25
            self.__atk+=a
            self.__hp+=h
```

###  坏脾气

只有当前奇美拉不是最后一个奇美拉时才会发动技能

```python
# **坏脾气【发作，AT:2，HP:9】：**==自身工作时==：使`后一格`同伴`体力-1`
class Hpq(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=9
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身工作时
        if changed_attr=="work_num" and new_value>old_value and self.__on:
            #获得当前位置
            position=self.queue.members_list.index(self)
            #如果后面有同伴，则使后面同伴hp-1
            if position>0:
                self.queue.members_list[position-1].hp-=1
```

###  抗压包

使得同伴效率降增加并不会实际触发技能，因此可以直接操作，并不需要先记录需要加buff的奇美拉对象

```python
#**抗压包【熟练，2，5】：**==自身体力降低时==使`前后一格`同伴`效率+1`
class Kyb(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=5
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身体力降低时
        if changed_attr=="hp" and new_value<old_value and self.__on:
            #获得当前位置
            position=self.queue.members_list.index(self)
            l=len(self.queue.members_list.index(self))
            position_before=position+1
            position_after=position-1

            if position_before>=0 and position_before<l:
                self.queue.members_list[position_before].atk+=1
            if position_after >= 0 and position_after < l:
                self.queue.members_list[position_after].atk += 1
```

###  请假狂

```python
# **请假狂【装病，2，7】：**==自身体力降低后==，与`后一格`同伴`交换位置`，并使自身`效率+2`
class Qjk(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=7
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身体力降低时
        if changed_attr=="hp" and new_value<old_value and self.__on:
            #获得当前位置
            position=self.queue.members_list.index(self)
            #如果不在队列最后，则与后一格同伴交换位置，并使自身体力+2
            if position>0:
                self.queue.members_list[position-1],self.queue.members_list[position]=self.queue.members_list[position],self.queue.members_list[position-1]
                self.atk += 2
```

###  请假王

```python
# **请假王【开摆，6，3】**：==自身体力降低后==，与`后一格`同伴`交换位置`，并使自身`体力+3`
class Qjw(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=6
        self.__hp=3
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身体力降低时
        if changed_attr == "hp" and new_value < old_value and self.__on:
            # 获得当前位置
            position = self.queue.members_list.index(self)
            # 如果不在队列最后，则与后一格同伴交换位置
            if position > 0:
                self.queue.members_list[position - 1], self.queue.members_list[position] = self.queue.members_list[position], self.queue.members_list[position - 1]
                self.hp += 3
```

###  内卷王

```python
# **内卷王【激励，3，8】：**==自身完成工作时==：获得`效率+2`，`体力+3`
class Njw(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=8
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身完成工作时，
        if changed_attr=="complete_work_num" and new_value>old_value and self.__on:
            self.atk+=2
            self.hp+=3
```

###  受气包

```python
# **受气包【道歉，2，5】：** ==自身体力降低时==，使全局同伴`效率+1`
class Sqb(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=5
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身体力降低时
        if changed_attr == "hp" and new_value < old_value and self.__on:
            for i in self.queue.members_list:
                if i!=self:
                    i.atk+=1
```

###  跑路侠

跑路侠累到后和后一个同伴一起逃离工作，根据前面提到的“规则”，我们不直接修改后一个同伴的生命，而是修改on属性为False，在每回合结束后，会把所有on属性为False的奇美拉清理出队列。此外，为了确保跑路侠hp小于0后一定离场（后续其他奇美拉对他加hp也不起作用），我们增加了一个hp-100的语句，为了防止这个语句继续调用跑路侠的技能，跑路下的技能判断条件为，旧的hp>0，新的hp<1(<=0)。(==如果你还记得我们之前提到过的，在eval中用下划线修改私有属性并不会通知观察者，那么这里你就可以优雅的用`self.__hp+=100`==)

```python
# **跑路侠【怂恿，1，1】**：==自身累倒时==，和后一格同伴一起`逃离工作`，并使其他同伴`体力+8`
class Plx(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=1
        self.__hp=1
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #只监控自身的属性变化从而保证每回合只触发一次被动技能
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #自身累倒时
        if changed_attr == "hp" and new_value < 1 and old_vale>0 and self.__on:
            slef.__hp-=100
            position=self.queue.members_list.index(self)
            # 使得后一格同伴离场，不修改后一格同伴的生命值
            if position>0:
                self.queue.members_list[position-1].on=False
            # 使得其他同伴体力+8
            for i in range(len(self.queue.members_list)):
                if i<(position-1) or (i> position):
                    self.queue.members_list[i].hp+=8
                  
```

###  看乐子

正如上文提到的，对于同一个奇美拉，看乐子可能触发两次被动。这也是有道理的，奇美拉生命值小于0表示累倒了。但是同伴可以给他加buff，使她的hp>0，此时又充满活力了，所以可以再次工作累倒。

```python
# **看乐子【围观，3，3】**：==同伴累到后==，自身`效率+2`，`体力+2`
class Klz(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=3
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴累倒后
        if changed_attr == "hp" and new_value < 1 and old_vale>0 and self.__on:
            self.atk+=2
            self.hp+=2
```

###  背锅侠

```python
# **背锅侠【接锅，3 ，6：**==同伴累倒时==，使该同伴`体力+10`，自身逃离工作
class Bgx(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=6
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴累倒后
        if changed_attr == "hp" and new_value < 1 and old_vale>0 and self.__on:
            #同伴累到后体力为hp，不会出现负体力，但这里不要用等于10
            #可能会出现其他奇美拉也给他加血，并且先于该奇美拉。
            print(f"\t给{changed_obj.name}加buff，hp+10!")
            changed_obj.hp+=10
            #注意此时不能修改self.queue.remove_member，因为我们无法保证此时弱引用集合已经遍历完毕。
            #如果直接修改，可能会会导致集合在遍历过程中被修改了，因此我们需要保证所有的技能都执行完，才移除on属性为False的奇美拉。也就是在每回合最后才移除奇美拉。
            self.on=False
```

###  抢功劳

这里需要保证work的hp>0，道理也很简单，如果工作已经被完成了，尘埃落定，如何抢功劳呢？由于追加工作可能触发其他奇美拉的被动，因此我们先判断是否完成工作，然后再修改complete_work_num属性。

```python
# **抢功劳【独占，15，2：** ==同伴工作时==：若自身效率》=剩余工作进度，则进行`追加工作`完成该任务
class Qgl(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=15
        self.__hp=2
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴工作时，进行追加工作不算
        if changed_attr == "work_num" and (new_value-old_value)==1 and self.__on:
            #如果回合开始时的效率足以完成任务
            if self.__fixed_atk>=self.queue.work.hp and self.queue.work.hp>0:
                #进行一次追加攻击
                self.queue.work.hp-=self.__fixed_atk
                if self.queue.work.hp < 1:
                    #完成工作也可能触发其他同伴的技能，因此需要最后执行
                    self.complete_work_num += 1
                #追加攻击可能触发其他同伴的技能，导致继续工作一次，因此需要最后执行
                self.append_work_num+=1
```

###  急先锋

```python
# **急先锋【带头，2，5】：**==同伴工作或追加工作时==，自身与前一格同伴`交换位置`，并且`体力+6`
class Jxf(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=2
        self.__hp=5
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴工作或追加工作时，
        if (changed_attr =="work_num" or changed_attr=="append_work_num") and (new_value-old_value)==1:
            position=self.queue.members_list.index(self)
            #如果当前奇美拉不是第一个奇美拉
            if position<len(self.queue.members_list)-1:
                print(f"\t{self.name}与前一格奇美拉交换位置")
                #与前一格同伴交换位置
                self.queue.members_list[position],self.queue.members_list[position+1]=\
                self.queue.members_list[position+1],self.queue.members_list[position]
                self.hp+=6
```

###  说怪话

```python
# **说怪话【暗讽，14，1】：**==同伴完成工作时==，使该同伴`效率+4 `并发表自己的意见
class Sgh(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=14
        self.__hp=1
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴完成工作时
        if changed_attr == "complete_work_num" and (new_value-old_value)==1 and self.__on:
            #使该同伴效率+4
            changed_obj.atk+=4
            #发表锐评
            print(f"{self.name}对{changed_obj.name}发表了锐评")

```

###  帮倒忙

```python
# **帮倒忙【捣乱，-1，5】：**==同伴工作时==，自身进行一次`追加工作`
class Bdm(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=-1
        self.__hp=5
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴工作时候
        if changed_attr =="work_num" and (new_value-old_value)==1 and self.__on:
            #自身进行追加攻击,工作小于0的时候也可以继续追加攻击获得buff
            self.queue.work.hp-=self.__fixed_atk
            print(f"\t{self.name}进行一次追加攻击！")
            #追加攻击后立刻判断是否完成工作
            if self.queue.work.hp < 1:
                self.complete_work_num += 1
            self.append_work_num+=1
```

###  小夸夸

```python
# **小夸夸【鼓励，3，3】：**==同伴工作或追加工作时==，若同伴效率》5使其`效率+2 `
class Xkk(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=3
        self.__hp=3
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴工作或追加工作时
        if (changed_attr == "work_num" or changed_attr== "append_work_num") and (new_value-old_value)==1 and self.__on:
            #如果同伴效率>5，使效率+2
            if changed_obj.atk>5:
                #小夸夸监控所有队友的所有属性，因此修改atk也会进入小夸夸的eval但是不会执行任何语句。
                print(f"\t给{changed_obj.name}加buff，atk+2!")
                changed_obj.atk+=2
```

###  工作狂

```python
# **工作狂【争先 6，10】：**==同伴工作或追加工作时==，进行一次等于自身50%效率的`追加工作`
class Gzk(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=6
        self.__hp=10
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴工作或追加工作时
        if (changed_attr == "work_num" or changed_attr== "append_work_num") and (new_value-old_value)==1 and self.__on:
            #进行一次相当于自身50%效率的追加攻击
            self.queue.work.hp-=(self.__fixed_atk/2)
            print(f"\t{self.name}进行一次追加攻击！")
            if self.queue.work.hp<1:
                self.complete_work_num+=1
            self.append_work_num+=1
```

###  职业经理

```python
# **职业经理【自我驱动】：**==登场后==：使全体奇美拉`效率+3`，`体力+3`
class Zyjl(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=6
        self.__hp=10
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=0  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self!=changed_obj):
            return
        #同伴工作或追加工作时
        if changed_attr == "on" and old_value==False and self.__on:
            #使所有成员效率和体力都+3
            for i in self.queue.members_list:
                i.hp+=3
                i.atk+=3
```

###  严酷恶魔

```python
# **严酷恶魔【不准停！】：**奇美拉==完成工作后==，使其`效率+5`
class Ykem(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=6
        self.__hp=10
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=1  #监控自己以外的所有同伴
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):
        if(self==changed_obj):
            return
        #同伴完成工作后
        if changed_attr == "complete_work_num" and (new_value-old_value)==1 and self.__on:
            #使其效率+5
            changed_obj.atk+=5
```

### 职场清流 

```python
# **职场清流【抚慰之心】：**==登场后==：全体奇美拉`效率+2`。奇美==拉追加工作==后：使其`效率+1`
class Zcql(ChimerasEntity):
    __observed_attrs__ = ('atk', 'hp','episode','on','work_num','append_work_num','mode','skill','complete_work_num')
    def __init__(self, name):
        super().__init__(name)
        self.name=name
        self.__atk=6
        self.__hp=10
        self.__episode=0  #每回合开始都会先增加回合数
        self.__on=False  #是否在场，True为登场，刚开始的时候为False
        self.__work_num=0  #工作次数
        self.__append_work_num=0  #追加攻击次数
        self.__mode=2  #监控自己及其所有奇美拉
        self.__skill=True
        self.__complete_work_num = 0
        self.__fixed_atk=0
    @property
    def fixed_atk(self):
        return self.__fixed_atk
    def set_fix_atk(self):
        self.__fixed_atk=self.__atk
    def eval(self, changed_obj, changed_attr, old_value, new_value):

        #登场后，全体奇美拉效率+2
        if changed_attr == "on" and old_value==False and changed_obj==self and self.__on:
            for i in self.queue.members_list:
                print(f"\t给{i.name}加buff，atk+2!")
                i.atk+=2
        #同伴追加攻击后，使其效率+1
        if changed_attr == "append_work_num" and (new_value-old_value)==1 and changed_obj!=self and self.__on:
            print(f"\t给{changed_obj.name}加buff，{changed_attr} atk+1!")
            changed_obj.atk+=1
```



##  开始工作吧小奇美拉

我们把工作也定义成一个类，该类中仅有攻击力和生命值属性，同时设置这两个属性的property描述符。我们把所有的工作逻辑都集成在奇美拉队列类中，我们在该类中新增三个方法

1. work_once，选定第一个在场并且hp>0的奇美拉，使其进行一次工作
2. work_episode，执行一个工作回合，在该函数中处理每回合工作前和工作后的一些信息。例如工作前增加回合数，固定攻击力。工作后判断奇美拉是否应该离场
3. begin_work，该方法接受一个工作对象，然后循环调用work_episode直到完成工作或者所有奇美拉都累到了

**Task类**

```python
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
```



**begin_work：**

```python
class InteractionQueue:
    """管理相互观察的队列"""
	#......此处参见本系列的上一篇博文
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
```

**work_episode**

```python
class InteractionQueue:
    """管理相互观察的队列"""
	#......此处参见本系列的上一篇博文
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
```

**work_once**

```python
class InteractionQueue:
    """管理相互观察的队列"""
	#......此处参见本系列的上一篇博文
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
```

最后，给出我们非常简单的main函数，完结撒花，*★,°*:.☆(￣▽￣)/$:*.°★* 。🌸🌸🌸

```python
import time
import unittest
from observer import InteractionQueue, Task
from chimeras import *

if __name__=="__main__":
    queue=InteractionQueue()
    jxf=Jxf("急先锋")
    queue.add_member(jxf)
    gzk=Gzk("工作狂")
    queue.add_member(gzk)
    bdm=Bdm("帮倒忙")
    queue.add_member(bdm)
    xkk=Xkk("小夸夸")
    queue.add_member(xkk)
    bgx=Bgx("背锅侠")
    queue.add_member(bgx)
    zcql=Zcql("职场清流")
    queue.add_leader(zcql)
    work=Task(atk=5,hp=80)

    queue.begin_work(work)
```

##  没想到吧，我还在！（优化）

**不同的奇美拉应该监控特定属性：**回忆一下我们的元类和基类的实现，`__observed_attrs__`存放的更像是subject的主题，也就是其他奇美拉关注的属性。那么对于同一个奇美拉，不同的奇美拉可能观察该奇美拉的不同属性，这就需要属性分类。

我们可以把属性进行分类（或者说分级），相应的我们把observer也进行分类（和前面属性的分类是一一对应的）。在属性变化的时候，根据属性的级别，遍历不同的observer集合，调用被动技能和该属性有关的奇美拉的eval方法，而不是调用所有奇美的eval方法。



**有序弱引用：**我们在queue中保存所有对象的强引用（list保存）,此时我们必须手动调用queue的remove函数。如果我们打算在成员的析构函数中调用queue的remove函数就会出现一个奇怪的循环。如果我们忘记调用queue的remove_member函数，我们del成员，但是由于queue中保留着成员的引用，所以不会执行成员的析构函数。由于不会执行析构函数，所以queue中一直保留着成员的引用。解决办法可以采用**有序弱引用。**

我们需要自己基于weakref来实现一个有序弱引用类。这里给出基于有序字典来实现的思路：我们创建一个key为id（递增，）value为弱引用对象的有序字典。每次我们手动递增id。添加弱引用的时候需要判断该弱引用对象是否已经存在地点内。

[游戏开发实战（一）：Python复刻「崩坏星穹铁道」嗷呜嗷呜事务所---源码级解析该小游戏背后的算法与设计模式【纯原创】-CSDN博客](https://blog.csdn.net/coreyckw/article/details/148074894?spm=1001.2014.3001.5501)

[游戏开发实战（二）：Python复刻「崩坏星穹铁道」嗷呜嗷呜事务所---源码级解析该小游戏背后的算法与设计模式【纯原创】-CSDN博客](https://blog.csdn.net/coreyckw/article/details/148090861?spm=1001.2014.3001.5501)

[游戏开发实战（三）：Python复刻「崩坏星穹铁道」嗷呜嗷呜事务所---源码级解析该小游戏背后的算法与设计模式【纯原创】-CSDN博客](https://blog.csdn.net/coreyckw/article/details/148098460?spm=1001.2014.3001.5501)
