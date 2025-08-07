import pandas as pd
import numpy as np

np.random.seed(42)

platforms = ['Android', 'iOS', 'Both']
complexities = ['Simple', 'Medium', 'Complex']

def generate_data(n=500):
    data = []
    for _ in range(n):
        platform = np.random.choice(platforms)
        complexity = np.random.choice(complexities)
        auth = np.random.choice([0, 1])
        backend = np.random.choice([0, 1])
        payment = np.random.choice([0, 1])
        realtime = np.random.choice([0, 1])
        screens = np.random.randint(3, 30)
        duration = np.random.randint(4, 24)

        cost = 5000
        if platform == 'Both': cost += 3000
        elif platform == 'iOS': cost += 1000

        if complexity == 'Medium': cost += 4000
        elif complexity == 'Complex': cost += 8000

        cost += auth * 1000 + backend * 2000 + payment * 1500 + realtime * 2500
        cost += screens * 100
        cost += duration * 150

        data.append([platform, complexity, auth, backend, payment, realtime, screens, duration, cost])

    return pd.DataFrame(data, columns=[
        'platform', 'complexity', 'auth', 'backend', 'payment',
        'realtime', 'screens', 'duration', 'cost'
    ])

df = generate_data()
df.to_csv("app_cost_dataset.csv", index=False)
print("Dataset saved to app_cost_dataset.csv")
