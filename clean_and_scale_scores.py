import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    scores = np.array(scores, dtype=float)
    scores[scores < min_score] = min_score
    scores[scores > max_score] = max_score
    scaled= (scores - min_score) / (max_score - min_score)
    return scaled
scaled = clean_and_scale_scores([85,65,120,20,65,95,70], 50, 100)
print(scaled)
