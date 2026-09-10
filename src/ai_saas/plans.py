PLANS={
    "starter":{"seats":3,"ai_actions":1000,"features":{"rag"}},
    "pro":{"seats":20,"ai_actions":10000,"features":{"rag","agents","automation"}},
    "enterprise":{"seats":1000,"ai_actions":100000,"features":{"rag","agents","automation","sso"}},
}
def entitled(plan,feature):
    return feature in PLANS.get(plan,{}).get("features",set())
def limit(plan,key):
    return PLANS.get(plan,{}).get(key,0)
