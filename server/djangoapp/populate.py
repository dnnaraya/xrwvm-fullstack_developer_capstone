from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"make_name": "NISSAN",
         "description": "Great cars. Japanese technology"},
        {"make_name": "Mercedes",
         "description": "Great cars. German technology"},
        {"make_name": "Audi",
         "description": "Great cars. German technology"}, 
        {"make_name": "Kia",
         "description": "Great cars. Korean technology"},
        {"make_name": "Toyota",
         "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(make_name=data['make_name'],
                                   description=data['description']))
    print(car_make_instances)
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"model_name": "Pathfinder", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[0]},
      {"model_name": "Qashqai", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[0]},
      {"model_name": "XTRAIL", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[0]},
      {"model_name": "A-Class", "types": "SUV", 
       "year": 2023, "car_make": car_make_instances[1]},
      {"model_name": "C-Class", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[1]},
      {"model_name": "E-Class", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[1]},
      {"model_name": "A4", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[2]},
      {"model_name": "A5", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[2]},
      {"model_name": "A6", "types": "SUV", 
       "year": 2023, "car_make": car_make_instances[2]},
      {"model_name": "Sorrento", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[3]},
      {"model_name": "Carnival", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[3]},
      {"model_name": "Cerato", "types": "Sedan",
       "year": 2023, "car_make": car_make_instances[3]},
      {"model_name": "Corolla", "types": "Sedan",
       "year": 2023, "car_make": car_make_instances[4]},
      {"model_name": "Camry", "types": "Sedan",
       "year": 2023, "car_make": car_make_instances[4]},
      {"model_name": "Kluger", "types": "SUV",
       "year": 2023, "car_make": car_make_instances[4]},
      ]

    for data in car_model_data:
        CarModel.objects.create(model_name=data['model_name'],
                                car_make=data['car_make'],
                                types=data['types'],
                                year=data['year'])
