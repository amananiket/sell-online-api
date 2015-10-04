#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>

using namespace std;

vector< vector<int> > get_ways(int num_stairs) {
    //TODO Return a vector of vectors of ints representing
    //the different cominations of ways to climb num_stairs
    //stairs, moving up either 1, 2, or 3 stairs at a time.
    
    vector< vector<int> > row1, row2;
    vecotr<int> column, column2, column3, column4;
    
    if(num_stairs == 0){
        return row1.push_back(column);
        
    }else if(num_stairs >= 1){
        row1 = get_ways(num_stairs-1);
        
        for (int i = 0; i < row1.size(); i++){
            column = row1[i];
            column.push_back(1);
            row2.push_back(column);
        }
        
        return row2;
           
        
    
    }else if(num_stairs >= 2){
        
        row1 = get_ways(num_stairs-2);
        
        for (int i = 0; i < row1.size(); i++){
            column = row1[i];
            column.push_back(2);
            column2 = row1[i];
            column2.push_back(1);
            column2.push_back(1);
            row2.push_back(column);
            row2.push_back(column2);
        }
        
        return row2;
           
        
    
    }else if(num_stairs >= 3){
        
        row1 = get_ways(num_stairs-3);
        
        for (int i = 0; i < row1.size(); i++){
            column = row1[i];
            column.push_back(3);
            column2 = row1[i];
            column2.push_back(1);
            column2.push_back(1);
            column2.push_back(1);
            column3 = row1[i];
            column3.push_back(2);
            column3.push_back(1);
            column4 = row1[i];
            column4.push_back(1);
            column4.push_back(2);
            row2.push_back(column);
            row2.push_back(column2);
            row2.push_back(column3);
            row2.push_back(column4);
        }
        
        return row2;
           
}


int main(){
	int n;
	cin >> n;
	vector<vector<int>> pot;

	cout << endl;
	for (int i = 0; i < pot.size(); i++ ){
		for (int j = 0; j < pot[i].size(); j++){
			cout << pot[i][j] << "\t";
		}
		cout << endl;
	}

	return 0;

}