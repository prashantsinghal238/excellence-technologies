from urllib.request import urlopen,Request
import json
# QUES 1  MERGING COMMENTS WITH ITS POST 
def post_with_comment(post_url,comment_url):
    merged=[]
    posts=json.loads(urlopen(post_url).read())
    comments=json.loads(urlopen(comment_url).read())
    for post in posts:
        comm=""
        for comment in comments:
            if (post["id"]==comment["postId"]):
                comm=comment["body"]+","+comm[0:-1]     
        temp_dict=post
        temp_dict["body"]=comm
        merged.append(temp_dict)        
    output1=json.dumps(merged)
    return output1 
# QUES 2 CALCULATING TOTAL NO OF USER 
def total_user(page_url):
    tot_user=[]
    for _ in range(1,12+1):
        path=page_url+str(_)
        req = Request(path, headers={'User-Agent': 'prashant/2022'})
        data=json.loads( urlopen(req, timeout=10).read())
        for user in data["data"]:
            try:
             tot_user.append(user["id"])
            except:
                pass 
    no_of_user=len(list(set(tot_user))) 
    return no_of_user 
if __name__=='__main__':
    post_url = "https://my-json-server.typicode.com/typicode/demo/posts"
    comment_url = "https://my-json-server.typicode.com/typicode/demo/comments" 
    page_url="https://reqres.in/api/users?page="
    print("output for Ques1 \n",post_with_comment(post_url, comment_url))    
    print("output for Ques2 \n",total_user(page_url))           