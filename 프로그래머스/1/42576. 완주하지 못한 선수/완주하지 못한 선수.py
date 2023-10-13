def solution(participant, completion):
    participant_dict = {}
    for participant_person in participant:
        if participant_person in participant_dict:
            participant_dict[participant_person] += 1
        else:
            participant_dict[participant_person] = 1
    
    for participant_completion in completion:
        participant_dict[participant_completion] -= 1
    
    for name, value in participant_dict.items():
        if value != 0:
            return name