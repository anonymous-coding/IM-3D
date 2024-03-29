
for f in ["imagedream-p.mp4", "magic123.mp4", "syncdreamer.mp4", "zero123xl.mp4"]:
    for d in [
        'frog', 'crab', 'ghost', 'eagle', 'jacket', 'wolfgirl', 'bulldog', 'butterfly', 'bear', 'squirrel', 'monkey', 'armor', 'dragon', 
        'astronaut', 'pig', 'axe', 'mech', 'pile', 'chicken', 'corgi', 'gun', 'Daenerys', 'helmet', 'horse', 'house', 'katana', 'motorcycle', 
        'mrbean', 'operahouse', 'windmill', 'peacock', 'pikachu', 'saber', 'statue', 'trump', 'yoda', 'fan', 'tank', 'girl',
    ]:
        # print(f'ffmpeg -i {d}/{f} -filter:v "setpts=3*PTS" {d}/NEW--{f}')
        print(f'mv {d}/NEW--{f} {d}/{f}')