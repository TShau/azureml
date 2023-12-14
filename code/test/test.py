import json

from azureml.core import Webservice


def main(service):
    # Creating input data
    print("Creating input data")
    data = {"data": [[ 1,2,3,4 ], [ 10,9,8,7 ]]}
    input_data = json.dumps(data)

    # Calling webservice
    print("Calling webservice")
    output_data = service.run(input_data)
    predictions = output_data.get("predict")
    assert type(predictions) == list


if __name__ == "__main__":
    main()


def log_confusion_matrix(cm, labels):
    # log confusion matrix as object
    cm_json =   {
       'schema_type': 'confusion_matrix',
       'schema_version': 'v1',
       'data': {
           'class_labels': labels,
           'matrix': cm.tolist()
       }
    }
    run.log_confusion_matrix('confusion_matrix', cm_json)
    
    # log confusion matrix as image
    log_confusion_matrix_image(cm, labels, normalize=False, log_name='confusion_matrix_unnormalized', title='Confusion matrix')
    
    # log normalized confusion matrix as image
    log_confusion_matrix_image(cm, labels, normalize=True, log_name='confusion_matrix_normalized', title='Normalized confusion matrix')
