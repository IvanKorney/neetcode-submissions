class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false
        }

        const smap = {}
        const tmap = {}
        for(let i = 0; i < s.length; i++){
            smap[s[i]] = 1 + (smap[s[i]]||0)
            tmap[t[i]] = 1 + (tmap[t[i]]||0)
        }
        for(const key in smap){
            if(smap[key] !== tmap[key]){
                return false
            }
        }
        return true
    }
}
