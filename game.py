from keras.model import sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(units=9, input_dim=9))
model.add(Activation('relu'))
model.add(Dense(units=1))
model.add(Activation('softmax'))


def recursiveTrain(initial_position, inputs):
    for each empty location of the initial position
    { 
        put a piece of the current side at this location (and call the resulting position A)
        if after putting this piece, the cross side wins 
        { 
            reward = 1; 
        }
        else if the winning side is the circle
        {
            reward = 0;
        } 
        else 
        { 
            for each empty location of the position A
            { 
                put a piece of the opposite side at the location
                calculate the reward of doing this action by running this position through the neural network.
                if the current side is the cross, look for the maximum reward returned by the network. 
                else if the current side is the circle, look for the minimum reward.
             }
        }
        # Basically, given a position, tells which state will have maximum output
        train the neural network with (Position A and reward)
        call recursiveTrain with position A as the initial position, and the opposite side
    } 

if __name__ == "__main__":
    train();
