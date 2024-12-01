def solution(bandage, health, attacks):
    hp = health
    answer = 0
    attacks = sorted(attacks, key=lambda x: x[0])
    duration, tick_hp, bonus_hp = bandage
    ticks = 0
    time = 0
    end_time = attacks[-1][0]
    
    while time <= end_time:
        if attacks[0][0] == time:
            attack_time, damages = attacks.pop(0)
            hp -= damages
            ticks = 0
            if hp <= 0:
                hp = -1
                break
        else:
            ticks += 1
            hp = min(health, hp + tick_hp)
            if ticks == duration:
                hp = min(health, hp + bonus_hp)
                ticks = 0
            
        time += 1
    answer = hp
        
    return answer