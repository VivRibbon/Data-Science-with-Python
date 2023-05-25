import numpy as np

def calculate(nums):
    """The calculate function"""
    match len(nums):
        case 9:
            source_array = np.asarray(nums)
            source_array = np.reshape(source_array, (3, 3))

            results_dict = {
                "mean": [list(np.mean(source_array, axis=0)), list(np.mean(source_array, axis=1)), np.mean(source_array)],
                "variance": [list(np.var(source_array, axis=0)), list(np.var(source_array, axis=1)), np.var(source_array)],
                "standard deviation": [list(np.std(source_array, axis=0)), list(np.std(source_array, axis=1)), np.std(source_array)],
                "max": [list(np.max(source_array, axis=0)), list(np.max(source_array, axis=1)), np.max(source_array)],
                "min": [list(np.min(source_array, axis=0)), list(np.min(source_array, axis=1)), np.min(source_array)],
                "sum": [list(np.sum(source_array, axis=0)), list(np.sum(source_array, axis=1)), np.sum(source_array)]
            }

            return results_dict
        case _:
            raise ValueError("List must contain nine numbers.")

calculate([0,1,2,3,4,5,6,7,8])
