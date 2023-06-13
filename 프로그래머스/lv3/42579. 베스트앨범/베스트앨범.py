def solution(genres, plays):
    total = {genre: 0 for genre in list(set(genres))}
    
    for genre, play in zip(genres, plays):
        total[genre] += play
        
    total = list(total.items())
        
    # 플레이 횟수가 높은 순으로 정렬
    total.sort(key=lambda x: -x[1])
    
    # 장르별 플레이 횟수 배열
    playsOfGenre = {genre: [] for genre in list(set(genres))}
    
    index = 0
    for genre, play in zip(genres, plays):
        playsOfGenre[genre].append((index, play))
        index += 1
        
    for genre, plays_list in playsOfGenre.items():
        plays_list.sort(key=lambda x: -x[1])
        playsOfGenre[genre] = plays_list
            
    result = []
    for t in total:
        genre = t[0]
        
        selected = playsOfGenre[genre][:2]
        for sn, _ in selected:
            result.append(sn)
            
    return result        
        