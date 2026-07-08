from src.config import ACCOUNT_ALIASES
from src.preprocessing import aggregate_accounts
from rapidfuzz import process, fuzz

def alias_matching(df):
    df=df.copy()
    df['Account']=df['Account'].map(ACCOUNT_ALIASES).fillna(df['Account'])
    return df

def fuzzy_matching(gl_df,tb_df,threshold=90):
    gl_df=gl_df.copy()
    unique_names=tb_df['Account'].unique()
    for acc in gl_df.Account.unique():
        match=process.extractOne(
            query=acc,
            choices=unique_names,
            scorer=fuzz.WRatio,
        )
        if match is not None and  match[1]>=threshold:
            gl_df.loc[gl_df['Account']==acc,"Account"]=match[0]
    return gl_df

def match_accounts(gl_df,tb_df):
    gl_df=alias_matching(gl_df)
    tb_df=alias_matching(tb_df)
    matched_gl_df=fuzzy_matching(gl_df,tb_df)
    gl_aggregate=aggregate_accounts(matched_gl_df)
    tb_aggregate=aggregate_accounts(tb_df)
    return gl_aggregate,tb_aggregate
