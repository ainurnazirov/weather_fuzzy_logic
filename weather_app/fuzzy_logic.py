import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


temperature = ctrl.Antecedent(np.arange(-45, 40, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')
pressure = ctrl.Antecedent(np.arange(740, 765, 1), 'pressure')
precipitation = ctrl.Consequent(np.arange(0, 100, 1), 'precipitation')

precipitation['low'] = fuzz.trimf(precipitation.universe, [0, 0, 40])
precipitation['medium'] = fuzz.trimf(precipitation.universe, [0, 40, 70])
precipitation['high'] = fuzz.trimf(precipitation.universe, [40, 70, 100])

temperature['low'] = fuzz.trimf(temperature.universe, [-45, -45, 0])
temperature['medium'] = fuzz.trimf(temperature.universe, [-45, 0, 20])
temperature['high'] = fuzz.trimf(temperature.universe, [0, 20, 40])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 34])
humidity['medium'] = fuzz.trimf(humidity.universe, [0, 34, 68])
humidity['high'] = fuzz.trimf(humidity.universe, [34, 68, 100])

pressure['low'] = fuzz.trimf(pressure.universe, [740, 740, 750])
pressure['medium'] = fuzz.trimf(pressure.universe, [740, 750, 754])
pressure['high'] = fuzz.trimf(pressure.universe, [750, 754, 765])

rule1 = ctrl.Rule(temperature['low'] & pressure['low'] & humidity['low'], precipitation['low'])
rule2 = ctrl.Rule(temperature['low'] & pressure['low'] & humidity['medium'], precipitation['medium'])
rule3 = ctrl.Rule(temperature['low'] & pressure['low'] & humidity['high'], precipitation['high'])
rule4 = ctrl.Rule(temperature['low'] & pressure['medium'] & humidity['low'], precipitation['medium'])
rule5 = ctrl.Rule(temperature['low'] & pressure['medium'] & humidity['medium'], precipitation['medium'])
rule6 = ctrl.Rule(temperature['low'] & pressure['medium'] & humidity['high'], precipitation['high'])
rule7 = ctrl.Rule(temperature['low'] & pressure['high'] & humidity['low'], precipitation['low'])
rule8 = ctrl.Rule(temperature['low'] & pressure['high'] & humidity['medium'], precipitation['low'])
rule9 = ctrl.Rule(temperature['low'] & pressure['high'] & humidity['high'], precipitation['medium'])

rule10 = ctrl.Rule(temperature['medium'] & pressure['low'] & humidity['low'], precipitation['low'])
rule11 = ctrl.Rule(temperature['medium'] & pressure['low'] & humidity['medium'], precipitation['medium'])
rule12 = ctrl.Rule(temperature['medium'] & pressure['low'] & humidity['high'], precipitation['high'])
rule13 = ctrl.Rule(temperature['medium'] & pressure['medium'] & humidity['low'], precipitation['medium'])
rule14 = ctrl.Rule(temperature['medium'] & pressure['medium'] & humidity['medium'], precipitation['medium'])
rule15 = ctrl.Rule(temperature['medium'] & pressure['medium'] & humidity['high'], precipitation['high'])
rule16 = ctrl.Rule(temperature['medium'] & pressure['high'] & humidity['low'], precipitation['low'])
rule17 = ctrl.Rule(temperature['medium'] & pressure['high'] & humidity['medium'], precipitation['low'])
rule18 = ctrl.Rule(temperature['medium'] & pressure['high'] & humidity['high'], precipitation['medium'])

rule19 = ctrl.Rule(temperature['high'] & pressure['low'] & humidity['low'], precipitation['low'])
rule20 = ctrl.Rule(temperature['high'] & pressure['low'] & humidity['medium'], precipitation['medium'])
rule21 = ctrl.Rule(temperature['high'] & pressure['low'] & humidity['high'], precipitation['high'])
rule22 = ctrl.Rule(temperature['high'] & pressure['medium'] & humidity['low'], precipitation['medium'])
rule23 = ctrl.Rule(temperature['high'] & pressure['medium'] & humidity['medium'], precipitation['medium'])
rule24 = ctrl.Rule(temperature['high'] & pressure['medium'] & humidity['high'], precipitation['high'])
rule25 = ctrl.Rule(temperature['high'] & pressure['high'] & humidity['low'], precipitation['low'])
rule26 = ctrl.Rule(temperature['high'] & pressure['high'] & humidity['medium'], precipitation['low'])
rule27 = ctrl.Rule(temperature['high'] & pressure['high'] & humidity['high'], precipitation['medium'])

precipitationing_ctrl = ctrl.ControlSystem([rule1,
                                            rule2,
                                            rule3,
                                            rule4,
                                            rule5,
                                            rule6,
                                            rule7,
                                            rule8,
                                            rule9,
                                            rule10,
                                            rule11,
                                            rule12,
                                            rule13,
                                            rule14,
                                            rule15,
                                            rule16,
                                            rule17,
                                            rule18,
                                            rule19,
                                            rule20,
                                            rule21,
                                            rule22,
                                            rule23,
                                            rule24,
                                            rule25,
                                            rule26,
                                            rule27])

precipitationing = ctrl.ControlSystemSimulation(precipitationing_ctrl)


def compute_fuzzy_logic(temperature, pressure, humidity):
    precipitationing.input['temperature'] = temperature
    precipitationing.input['pressure'] = pressure
    precipitationing.input['humidity'] = humidity

    precipitationing.compute()

    return precipitationing.output['precipitation']
