from job import Warrior, Wizard

# ============================
# 사용 예제
# ============================
arthur = Warrior('아더')

arthur.attack()               # 기본 공격 (무기 없음)
arthur.equip_weapon("지팡이")  # 장착 실패
arthur.equip_weapon("쌍검")    # 장착 성공
arthur.attack()                # 기본 공격 (무기 장착)
arthur.use_skill()             # 장착된 무기 스킬

merlin = Wizard("멀린")

merlin.attack()               # 기본 공격 (무기 없음)
merlin.equip_weapon("쌍검")    # 장착 실패
merlin.equip_weapon("마법봉")  # 장착 성공
merlin.attack()                # 기본 공격 (무기 장착)
merlin.use_skill()             # 장착된 무기 스킬
