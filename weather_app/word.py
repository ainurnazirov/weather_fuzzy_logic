def prediction_word(prediction):
    if prediction < 33:
        return 'Осадки не ожидаются'
    elif prediction < 67:
        return 'Низкая вероятность осадков'
    else:
        return 'Ожидаются осадки'
