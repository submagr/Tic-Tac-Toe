#include<iostream>
#include<exception>
#include<tuple>
#include<string>
using namespace std;

class noWinner: public exception{
    virtual const char* what() const throw()
    {
        return "No winner yet";
    }
};

class notOccupied: public exception{
    virtual const char * what() const throw(){
        return "Not occupied yet";
    }
};


class Agent{
public:
    string _agentName;
    char _symbol;
    Agent(string agentName, char symbol):_agentName(agentName), _symbol(symbol){
    }
    virtual ~Agent(){
    }
    virtual tuple<int, int> play() = 0;
};

// class BotAgent : public Agent{
// public:
//     BotAgent(string agentName, char symbol):Agent(agentName, symbol){
//     }
// };

class HumanAgent : public Agent{
public:
    HumanAgent(string agentName, char symbol):Agent(agentName, symbol){
    }

    tuple<int, int> play(){
        int i, j;
        cout << _agentName << " turn, Please enter your move: ";
        cin >> i;
        cin >> j;
        cout << i << " " << j << endl;
        return make_tuple(i, j);
    }
};

// <There should be a class called board game>
class Board{
    int board[3][3];
    Agent *_zero;
    Agent *_cross;
    bool checkRow(int i, int j){
        return board[i][j] == board[i][(j+1)%3] and board[i][(j+1)%3] == board[i][j+2%3];
    }
    bool checkCol(int i, int j){
        return board[i][j] == board[(i+1)%3][j] and board[(i+1)%3][j] == board[i+2%3][j];
    }
    bool onDiag(int i, int j){
        return (i+j)==(3-1);
    }
    bool checkDiag(int i, int j){
        if(onDiag(i, j)){
            int n=3;
            bool isRightDiag =  (board[i][j] == board[(i+1)%n][(j+1)%n] and board[(i+1)%n][(j+1)%n] == board[(i+2)%n][(j+2)%n]) ;
            bool isLeftDiag = (board[i][j] == board[(i+1)%n][(n+j-1)%n] and board[(i+1)%n][(n+j-1)%n] == board[(i+2)%n][(n+j-2)%n]);
            return isLeftDiag or isRightDiag;
        }
        return false;
    }
    bool checkMatch(int i, int j){
        if(board[i][j] == 0){
            return 0;
        }
        return checkRow(i, j) or checkCol(i, j) or checkDiag(i, j);
    }
    bool isEmpty(){
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                if(board[i][j] == 0){
                    return true;
                }
            }
        }
        return false;
    }
public:
    Board(Agent *zero, Agent *cross): _zero(zero), _cross(cross){
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                board[i][j] = 0;
            }
        }
    }
    virtual ~Board(){
    }

    bool isOver(){
        int winner = checkWin();
        if(winner != 0){
            cout << winner << " won" << endl;
            return true;
        }
        else if(!isEmpty()){
            cout << "Draw" << endl;
            return true;
        }
        return false;
    }

    int checkWin(){
        if(checkMatch(0,0)){
            return board[0][0];
        }
        else if(checkMatch(1,1)){
            return board[1][1];
        }else if(checkMatch(2,2)){
            return board[2][2];
        }else{
            return 0; // Nobody won
        }
    }

    bool move(int agent, int i, int j){
        if(board[i][j] == 0){
            board[i][j] = agent;
            return true;
        }
        return false;
    }
    void gamePlay(){
        int turn = 1;
        while(!isOver()){
            int i, j;
            if(turn==1){
                tie(i,j) = _zero->play();
            }else{
                tie(i,j) = _cross->play();
            }

            if(move(turn, i, j)){
                display();
                if(turn==1)
                    turn = -1;
                else{
                    turn = 1;
                }
            }else{
                cout << "( " << i << ", "<< j<<") Already occupied" << endl;
            }
        }
    }
    void display(){
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                cout << "\t" << board[i][j];
            }
            cout << endl;
        }
    }
};

int main(){
    Agent *zero = new HumanAgent("zero", '0');
    Agent *cross = new HumanAgent("cross", 'X');
    Board myBoard(zero, cross); 
    myBoard.gamePlay();
    return 0;
}
