from django.shortcuts import render
from .forms import *
from .fuzzy_logic import compute_fuzzy_logic
from .machine_learning import compute_machine_learning
from .word import prediction_word


def index(request):

    if request.method == "POST":
        parameters = ParametersForm(request.POST)
        if parameters.is_valid():
            temperature = float(parameters.cleaned_data.get('temperature'))
            pressure = float(parameters.cleaned_data.get('pressure'))
            humidity = float(parameters.cleaned_data.get('humidity'))
            prediction_fuzzy_logic = compute_fuzzy_logic(temperature, pressure, humidity)
            prediction_fuzzy_logic_word = prediction_word(prediction_fuzzy_logic)
            prediction_machine_learning = compute_machine_learning(temperature, pressure, humidity)
            prediction_machine_learning_word = prediction_word(prediction_machine_learning)
            return render(request, 'index.html', {'form': parameters, 'prediction_fuzzy_logic': prediction_fuzzy_logic,
                                                  'prediction_fuzzy_logic_word': prediction_fuzzy_logic_word,
                                                  'prediction_machine_learning': prediction_machine_learning,
                                                  'prediction_machine_learning_word': prediction_machine_learning_word})
    else:
        parameters = ParametersForm()

    return render(request, 'index.html', {'form': parameters})
