class Solution {
public:
    void connect(int i, std::set<int>& s, std::unordered_map<int,std::vector<int>>& dep){
        s.insert(i);
        if(dep.count(i)){ 
            for(int node : dep.at(i)){
                if (s.find(node) == s.end()){
                    connect(node,s,dep);
                }
            }
        }
        
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        std::unordered_map<int,std::vector<int>> dep;
        for(const auto& edge : edges){
            dep[edge[0]].push_back(edge[1]);
            dep[edge[1]].push_back(edge[0]);
        }
        int res = 0;
        std::set<int> s;
        for(int i = 0; i < n; i++){
            if (s.find(i) == s.end()){
                res += 1;
                connect(i,s,dep);
            }
        }
        return res;
    }
};
