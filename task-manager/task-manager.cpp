#include<iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <filesystem>
#include <chrono>
#include <thread>
#include <unistd.h>

using namespace std;
int read_cpu();
int read_ram();
int read_ssd();
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
int read_cpu(){
    return idle, total;
}
