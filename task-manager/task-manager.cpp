#include<iostream>
using namespace std;
void read_cpu();
void read_ram();
void read_ssd();
void clear_screen();
int main(){
    ifstream file("/proc/stat");
    string line;
    if(!file.is_open()){
        cout<<"Cannot open /proc/stat\n";
        return 1;
    }
    getline(file, line);
    cout<<line<<endl;

    return 0;
}
