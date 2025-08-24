import streamlit as st

st.set_page_config(page_title="📝 My Blog App", layout="centered")

st.title("📝 Write a Blog")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'blog_title' not in st.session_state:
    st.session_state.blog_title = ""
if 'blog_content' not in st.session_state:
    st.session_state.blog_content = ""

if not st.session_state.submitted:
    st.subheader("✍️ Enter your blog")
    title = st.text_input("Title of the blog")
    content = st.text_area("Content of the blog", height=300)
    if st.button("Submit"):
        if title and content:
            st.session_state.blog_title = title
            st.session_state.blog_content = content
            st.session_state.submitted = True
        else:
            st.warning("Please fill out both the title and content!")
else:
    st.subheader("📄 Your Blog Post")
    st.markdown(f"## {st.session_state.blog_title}")
    st.markdown(st.session_state.blog_content)

    st.markdown("---")
    st.subheader("💬 Comment Section")
    comment = st.text_input("Leave your comment below:")
    if comment:
        st.success(f"Your comment: {comment}")

    if st.button("📝 Write Another Blog"):
        st.session_state.submitted = False
        st.session_state.blog_title = ""
        st.session_state.blog_content = ""
