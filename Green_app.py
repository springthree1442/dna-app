import streamlit as st
import matplotlib.pyplot as plt

# 분석 로직
def compare(ref, seq):
    mutations = []
    i = j = 0
    pos = 1
    while i < len(ref) and j < len(seq):
        if ref[i].upper() != seq[j].upper():
            mutations.append((pos, ref[i].upper(), seq[j].upper(), 'substitution'))
        i += 1
        j += 1
        pos += 1
    while i < len(ref):
        mutations.append((pos, ref[i].upper(), '-', 'deletion'))
        i += 1
        pos += 1
    while j < len(seq):
        mutations.append((pos, '-', seq[j].upper(), 'insertion'))
        j += 1
        pos += 1
    return mutations

def summarize(mutations, length):
    result = []
    for pos, ref_base, seq_base, mtype in mutations:
        result.append(f"{pos} {mtype.upper()} {ref_base}>{seq_base}")
    result.append(f"\nTotal: {len(mutations)}")
    result.append(f"Ratio: {(len(mutations)/length)*100:.2f}%")
    return result

def visualize(mutations, length):
    if not mutations:
        return None
    positions = [pos for pos, _, _, _ in mutations]
    fig, ax = plt.subplots(figsize=(8, 1))
    ax.eventplot(positions, orientation='horizontal', colors='#497325')
    ax.set_xlim(1, length + 1)
    ax.set_xlabel("Position")
    ax.set_yticks([])
    return fig

# --- Streamlit UI 구성 ---
st.set_page_config(layout="wide")
st.markdown("<h1 style='color:#497325;'>DNA Mutation Analyzer</h1>", unsafe_allow_html=True)

# 입력 & 출력 칼럼
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color:#497325;'>Input Sequences</h3>", unsafe_allow_html=True)
    ref = st.text_area("Reference Sequence (ref)", height=150)
    seq = st.text_area("Mutated Sequence (seq)", height=150)

    # 사용자 정의 버튼 스타일 적용
    analyze = st.markdown(
        f"""
        <style>
        .green-btn {{
            background-color: #a8c98c;
            color: white;
            border: none;
            padding: 0.6em 1.2em;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
        }}
        </style>
        <form action="" method="get">
            <button class="green-btn" type="submit">Analyze</button>
        </form>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown("<h3 style='color:#497325;'>Results</h3>", unsafe_allow_html=True)
    # 실제 분석은 text 입력이 trigger
    if ref and seq:
        mutations = compare(ref, seq)
        results = summarize(mutations, len(ref))
        for line in results:
            st.text(line)
        fig = visualize(mutations, len(ref))
        if fig:
            st.pyplot(fig)
