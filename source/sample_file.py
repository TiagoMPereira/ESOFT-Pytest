from source.elevador.elevador import Elevador
e = Elevador()
def load_data():
    # This should be mocked as it is a dependency
    return 1

def dummy_function():
    # This is the desired function we are testing
    return e.mover(1)

if __name__ == "__main__":
    print(dummy_function())