from DRecPy.Recommender.Baseline import UserKNN
from DRecPy.Dataset import get_full_dataset
from DRecPy.Evaluation.Processes import ranking_evaluation
from DRecPy.Evaluation.Splits import matrix_split
from DRecPy.Evaluation.Metrics import precision
from DRecPy.Evaluation.Metrics import recall
from DRecPy.Evaluation.Metrics import ndcg

ds = get_full_dataset('ml-100k')

ds_train, ds_test = matrix_split(ds, user_test_ratio=0.2, item_test_ratio=0.2, seed=15,
                                 verbose=False)

# cosine sim
knn = UserKNN(k=10, m=0, sim_metric='cosine_cf', shrinkage=None, seed=15, use_averages=False, verbose=True)
knn.fit(ds_train)

evaluation = ranking_evaluation(knn, ds_test, interaction_threshold=5, k=list(range(1, 11)),
                                generate_negative_pairs=False, n_pos_interactions=None,
                                n_neg_interactions=None, seed=15, verbose=True,
                                metrics={'P': (precision, {}),  'R': (recall, {}), 'NDCG': (ndcg, {})})
print('cosine sim', evaluation)

# jaccard sim
knn = UserKNN(k=10, m=0, sim_metric='jaccard', shrinkage=None, seed=15, use_averages=False, verbose=True)
knn.fit(ds_train)

evaluation = ranking_evaluation(knn, ds_test, interaction_threshold=5, k=list(range(1, 11)),
                                generate_negative_pairs=False, n_pos_interactions=None,
                                n_neg_interactions=None, seed=15, verbose=True,
                                metrics={'P': (precision, {}),  'R': (recall, {}), 'NDCG': (ndcg, {})})
print('jaccard sim', evaluation)

# msd sim
knn = UserKNN(k=10, m=0, sim_metric='msd', shrinkage=None, seed=15, use_averages=False, verbose=True)
knn.fit(ds_train)

evaluation = ranking_evaluation(knn, ds_test, interaction_threshold=5, k=list(range(1, 11)),
                                generate_negative_pairs=False, n_pos_interactions=None,
                                n_neg_interactions=None, seed=15, verbose=True,
                                metrics={'P': (precision, {}),  'R': (recall, {}), 'NDCG': (ndcg, {})})
print('msd sim', evaluation)


# pearson corr sim
knn = UserKNN(k=10, m=0, sim_metric='pearson', shrinkage=None, seed=15, use_averages=False, verbose=True)
knn.fit(ds_train)

evaluation = ranking_evaluation(knn, ds_test, interaction_threshold=5, k=list(range(1, 11)),
                                generate_negative_pairs=False, n_pos_interactions=None,
                                n_neg_interactions=None, seed=15, verbose=True,
                                metrics={'P': (precision, {}),  'R': (recall, {}), 'NDCG': (ndcg, {})})
print('pearson corr sim', evaluation)