
class Charater:

    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.weapon = None

    def attack(self):
        print(self.name)
        self.job.attack()


    def equip_weapon(self, weapon):
        # if self.job이 weapon을 안받아드려? 그럼 못껴
        if type(weapon) not in self.job.allow_weapons:
            # is_instance() 함수가 존재해요 -> 이거를 사용하는게 좀 더 안전한 방법
            print('착용 불가능합니다')
            return
        print(f'{weapon.name} 무기를 착용했습니다!')
        self.weapon = weapon

    def use_skill(self):
        # weapon에 따라 달라집니다.
        if self.weapon is not None:
            self.weapon.skill()
            return
        print('착용된 무기가 없어서 스킬 못써요!')
        