from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
true_labels = [0, 1, 1, 0, 1, 1, 0, 1]
predicted_labels = [0, 1, 0, 0, 1, 1, 0, 1]

accuracy = accuracy_score(true_labels, predicted_labels)
print(f'Accuracy: {accuracy:.2f}')

precision = precision_score(true_labels, predicted_labels)
print(f'Precision: {precision:.2f}')

recall = recall_score(true_labels, predicted_labels)
print(f'Recall: {recall:.2f}')