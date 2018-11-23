

from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

def calAuc(filename):
    y_scores, y_true = [], []

    for line in open(filename, 'r'):
        ys,yt = line.split("\t")
        ys = float(ys)
        yt = float(yt[:-1])
        if yt == -1:
            yt = 0
        y_scores.append(ys)
        y_true.append(yt)

    auc = roc_auc_score(y_true, y_scores)
    print 'auc =', auc

    correct,wrong = 0,0
    for i in range(len(y_scores)):
        y_hat= 1.0 if y_scores[i] > 0.5 else 0.0
        if y_hat == y_true[i]:
            correct += 1
        else:
            wrong += 1
    #print "correct ratio", 1.0 * correct / (correct + wrong)

    threshold = 0.5
    y_pred = []
    for i in range(len(y_scores)):
        y_hat = 1.0 if y_scores > threshold else 0.0
        y_pred.append(y_hat)

    recall = recall_score(y_true, y_pred, average='micro')  # 'micro','weighted','samples' binary
    #print('recall_score', recall)

    precision = precision_score(y_true, y_pred, average='micro')
    #print('precision_score', precision)

    return auc

if __name__ == '__main__':

    filename = "pred_target.txt"
    print "auc", calAuc(filename)


    s1 = "prec_target_sgd_1108_3/prec_target_sgd"
    s3 = ".txt"
    auc,count = 0,0
    for i in range(0,400):
        if i % 10 ==0:
            filename = s1 + str(i) + s3
            auc += calAuc(filename)
            count += 1
    avgauc = auc / count
    print('avgauc',avgauc)






