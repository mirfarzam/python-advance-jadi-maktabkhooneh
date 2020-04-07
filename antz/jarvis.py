from antz.models import Car
import numpy as np
from sklearn import linear_model
from joblib import dump, load

def linearReressionModel():
  reg = linear_model.LinearRegression()
  x_train_array = np.empty([1,4])
  cars = Car.objects.exclude(price__isnull=True).exclude(kilometer__isnull=True)
  number_of_rows = cars.count()
  x_train_array = np.zeros((number_of_rows, 5))
  y_train_array = np.zeros(number_of_rows)
  i = 0
  for car in cars:
    temp_trim = car.trim.id if car.trim != None else 0
    temp_row = [car.brand.id, car.model.id, temp_trim, car.year, car.kilometer]
    x_train_array[i,:] = temp_row
    y_train_array[i] = car.price
    i += 1
  reg.fit(x_train_array, y_train_array)
  dump(reg, './manhatan/price_predicting_model.joblib')

linearReressionModel()