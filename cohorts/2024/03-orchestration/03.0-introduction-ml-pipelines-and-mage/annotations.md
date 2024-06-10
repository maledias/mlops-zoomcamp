# Introduction
The idea of this module is to take a previously built notebook with a lot of experiments and turn it into something that can be easily run, somehting that is reproducible, parametrized and so on.

# What is a training pipeline?
A sequence of steps that we execute in order to train a ML model.

# The need for a trainig pipeline
Having the code to train and save (upload the model to a model registry) a model in a jupyter notebook is not the best way to do it. It is not reliable and reproducible.

# Example ML workflow
download the data (ingestion) -> transforming (filtering, aggregating, removing outliers, etc) the data -> data preparation (feature engineering) -> hyper parameter tuning -> train the final mode (once we find the best parameters in the last step) and upload the model to a model registry

# Building an ML pipeline
The first step is to transform the notebook into a python script.
Having a python script already makes it much more maintainable and reliable.
Code is split in functions, functions can be tested and so on.

But just having a python script is not enough... how do we schedule the execution of this script? how do we manage multiple ml pipelines? how to deploy the script? how to allow collaboration? how to scale having multiple jobs? how to add retry mechanisms? what if one of the steps fail?

That's why we usually use tools for workflow orchestration. THese tools usualy takes care of everything mentioned above.

There are multiple tools for that:
- airflow (general purpose)
- prefect (general purpose)
- mage (general purpose)
- Kubleflow pipelines (ML focused)
- MLflow pipelines (ML focused)
...




