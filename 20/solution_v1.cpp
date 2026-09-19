class Solution {
public:
    bool isValid(string s) {
    stack<char> st;
    bool res = true;
    for (char c : s)
    {
        if(c=='(' || c=='[' || c=='{')
        {st.push(c);}

        else if(c==')' || c==']' || c=='}')
        {
            if(st.empty())
            {
                res = false;
                break;
            }
            char top = st.top();

            if((c==')' && top!='(') || (c==']' && top!='[') || (c=='}' && top!='{'))
            {
                res = false;
                break;
            }

            st.pop();
        }
    }
    if(!st.empty())
    {res = false;}
    return res;

    }
};