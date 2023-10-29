def solution(genres, plays):
    answer = []
    info_dict = {}
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre in info_dict:
            info_dict[genre][0] += play
            for idx_song, song in enumerate(info_dict[genre][1:]):
                if play > song[1]:
                    info_dict[genre].insert(idx_song+1, (i, play))
                    break
            if len(info_dict[genre]) > 3:
                info_dict[genre].pop()
                
            if len(info_dict[genre]) < 3:
                info_dict[genre].append((i, play))
        else:
            info_dict[genre] = [play, (i, play)]
            
    sorted_list = sorted(info_dict.items(), reverse=True, key=lambda x: x[1][0])
    
    for sorted_genre_info in sorted_list:
        for sorted_song_info in sorted_genre_info[1][1:]:
            answer.append(sorted_song_info[0])
        
    return answer