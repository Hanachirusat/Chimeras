#奇美拉基类
from abc import ABC,abstractmethod
from observer import ChimerasEntity,InteractionQueue
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

# **小团体【排外，3，3】：** ==每回合开始时==，使前两格同伴`效率+1`，其余同伴`体力-1`
class Xtt(ChimerasEntity):
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


# **抗压包【熟练，2，5】：**==自身体力降低时==使`前后一格`同伴`效率+1`
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
        if changed_attr == "hp" and new_value < 1 and old_value>0 and self.__on:
            position=self.queue.members_list.index(self)
            # 使得后一格同伴离场，不修改后一格同伴的生命值
            if position>0:
                self.queue.members_list[position-1].on=False
            # 使得其他同伴体力+8
            for i in range(len(self.queue.members_list)):
                if i<(position-1) or (i> position):
                    self.queue.members_list[i].hp+=8

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
            # 防御性编程，可能会出现其他奇美拉也给他加血，并且先于该奇美拉。
            print(f"\t给{changed_obj.name}加buff，hp+10!")
            changed_obj.hp+=10
            #注意此时不能修改self.queue.remove_member，因为调用这个方法会修改其他类的若引用观察集
            #会导致集合在遍历过程中被修改了，因此我们需要保证所有的技能都执行完，也就是在每回合最后才能
            #移动成员。
            self.on=False

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
            if self.__fixed_atk>=self.queue.work.hp:
                #进行一次追加攻击
                self.queue.work.hp-=self.__fixed_atk
                if self.queue.work.hp < 1:
                    #完成工作也可能触发其他同伴的技能，因此需要最后执行
                    self.complete_work_num += 1
                #追加攻击可能触发其他同伴的技能，导致继续工作一次，因此需要最后执行
                self.append_work_num+=1

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

if __name__=="__main__":
    #奇美拉队列
    print(2%2)