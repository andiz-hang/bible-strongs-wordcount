import a_fetch_passage as a, b_clean_text as b, c_wordcount as c

if __name__ == "__main__":
    ref = a.get_ref_from_cl()
    a.run(ref)
    b.run()
    c.run()