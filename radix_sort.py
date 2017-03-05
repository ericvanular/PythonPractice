#https://www.interviewcake.com/question/python/top-scores

unsorted_scores = [37, 89, 41, 65, 91, 53]
highest_possible_score = 100

def sort_scores(unsorted_scores, highest_possible_score):
    scores_dict = dict()
    for i in range(highest_possible_score + 1):
        scores_dict[i] = []
        
    for score in unsorted_scores:
        scores_dict[score].append(score)
        
    sorted_scores = []
    
    for i in range(highest_possible_score + 1):
        for score in scores_dict[i]:
            sorted_scores.append(score)
    
    return sorted_scores
    

print sort_scores(unsorted_scores, highest_possible_score)        

