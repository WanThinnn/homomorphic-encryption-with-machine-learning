import sys
import time
import numpy as np

try:
    import concrete.ml
    from concrete.fhe import Configuration
    from concrete.ml.sklearn.svm import LinearSVC
    
    config = Configuration(use_gpu=True)
    print(f"Concrete ML version: {concrete.ml.__version__}")
    print(f"GPU Support requested in config: {config.use_gpu}")
    
    # Try a quick compilation
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    
    model = LinearSVC(n_bits=4)
    model.fit(X, y)
    
    t0 = time.perf_counter()
    model.compile(X, configuration=config)
    print(f"Compilation with GPU config took {time.perf_counter()-t0:.2f}s")
    
    # Try inference
    t0 = time.perf_counter()
    y_pred = model.predict(X[:1], fhe="execute")
    print(f"GPU FHE Inference took {time.perf_counter()-t0:.2f}s")
    print("SUCCESS: FHE executed on GPU (if backend supported it without falling back)")

except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")
