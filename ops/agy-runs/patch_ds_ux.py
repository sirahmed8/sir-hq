import re

path = r'D:\Projects\SIR Study\guides\data-structures.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for: .option-btn.selected, .quiz-score-banner, .flashcards-mastery-banner, .btn-copy-code, .inline-warn
new_css = '''
        /* Option Selected State (Pre-check) */
        .option-btn.selected {
            background: rgba(56, 189, 248, 0.16);
            border-color: var(--primary);
            color: #FFFFFF;
            box-shadow: 0 0 0 1px var(--primary);
        }

        /* Quiz Score & Mastery Banners */
        .quiz-score-banner, .flashcards-mastery-banner {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 16px 20px;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .score-info, .mastery-info {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-main);
        }

        .score-val, #mastery-count {
            font-family: var(--font-mono);
            color: var(--accent-green);
            font-size: 1.05rem;
            font-variant-numeric: tabular-nums;
        }

        .score-progress-track, .mastery-track {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border);
            border-radius: 999px;
            height: 10px;
            overflow: hidden;
            width: 100%;
        }

        .score-progress-fill, .mastery-fill {
            background: linear-gradient(90deg, var(--primary) 0%, var(--accent-green) 100%);
            height: 100%;
            width: 0%;
            border-radius: 999px;
            transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .btn-reset-quiz {
            align-self: flex-start;
            background: rgba(244, 63, 94, 0.1);
            color: #FDA4AF;
            border: 1px solid rgba(244, 63, 94, 0.3);
            border-radius: var(--radius-sm);
            padding: 6px 14px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: var(--transition);
        }
        .btn-reset-quiz:hover {
            background: rgba(244, 63, 94, 0.2);
        }

        /* Flashcard Mastery Tag & Buttons */
        .flashcard.mastered {
            border-color: rgba(52, 211, 153, 0.5);
            box-shadow: 0 0 15px -3px rgba(52, 211, 153, 0.2);
        }

        .mastery-controls {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            margin-top: 10px;
            padding-top: 8px;
            border-top: 1px dashed var(--border);
        }

        .btn-mastery {
            flex: 1;
            padding: 6px 8px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            border: 1px solid var(--border);
            background: var(--bg-card);
            color: var(--text-muted);
            transition: var(--transition);
            min-height: 38px;
        }
        .btn-mastery.btn-mastered {
            background: rgba(52, 211, 153, 0.15);
            color: #6EE7B7;
            border-color: rgba(52, 211, 153, 0.4);
        }
        .btn-mastery.btn-review {
            background: rgba(251, 191, 36, 0.1);
            color: #FDE68A;
            border-color: rgba(251, 191, 36, 0.4);
        }

        /* Floating Copy Code Button */
        pre {
            position: relative;
        }

        .btn-copy-code {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid var(--border);
            color: var(--text-muted);
            border-radius: 6px;
            padding: 5px 12px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            backdrop-filter: blur(8px);
            transition: var(--transition);
            z-index: 10;
        }
        .btn-copy-code:hover {
            color: #FFFFFF;
            background: var(--bg-card-hover);
            border-color: var(--primary);
        }
        .btn-copy-code.copied {
            background: rgba(52, 211, 153, 0.2);
            color: #6EE7B7;
            border-color: var(--accent-green);
        }

        /* Inline Warning */
        .inline-warn {
            color: #FBBF24;
            font-size: 0.82rem;
            font-weight: 700;
            margin-top: 6px;
            display: none;
            animation: fadeIn 0.2s ease-out;
        }
'''

content = content.replace('/* Practice Questions */', new_css + '\n        /* Practice Questions */')

# 2. Add Score Banner markup at beginning of #tab-quiz
quiz_banner_html = '''        <!-- TAB 6: PRACTICE QUESTIONS & EXAM BANK -->
        <section id="tab-quiz" class="tab-panel" role="tabpanel">
            <div class="content-card">
                <div class="card-header">
                    <h2 class="card-title">بنك الأسئلة والتدريبات الامتحانية التفاعلية</h2>
                    <span class="card-badge badge-green">15 سؤال شامل المنهج</span>
                </div>
                <p>اختبر معلوماتك بدقة؛ اختر إجابتك ثم اضغط على زر التحقق لمعرفة التفسير الأكاديمي واحتساب درجاتك الحية:</p>

                <!-- Live Quiz Score & Mastery Progress Tracker -->
                <div class="quiz-score-banner" id="quiz-score-banner">
                    <div class="score-info">
                        <span class="score-title">🏆 نتيجتك في الاختبار التجريبي:</span>
                        <span class="score-val" id="score-val">0 / 15 (0%)</span>
                    </div>
                    <div class="score-progress-track">
                        <div class="score-progress-fill" id="score-progress-fill"></div>
                    </div>
                    <button class="btn-reset-quiz" id="btn-reset-quiz">🔄 إعادة تعيين نتيجة الاختبار</button>
                </div>'''

content = re.sub(
    r'<!-- TAB 6: PRACTICE QUESTIONS & EXAM BANK -->\s*<section id="tab-quiz" class="tab-panel" role="tabpanel">[\s\S]*?<p>اختبر معلوماتك[\s\S]*?</p>',
    quiz_banner_html,
    content
)

# 3. Add Flashcards Mastery Banner markup in #tab-cards
cards_banner_html = '''        <!-- TAB 5: FLASHCARDS (25 KEY TERMS) -->
        <section id="tab-cards" class="tab-panel" role="tabpanel">
            <div class="content-card">
                <div class="card-header">
                    <h2 class="card-title">بطاقات الاستذكار السريع (Flashcards)</h2>
                    <span class="card-badge badge-rose">25 بطاقة مفاهيمية</span>
                </div>
                <p>اضغط على أي بطاقة أو استخدم مفتاح المسافة لقلبها وقراءة التعريف العلمي، ثم اضغط "أتقنتها" لحفظ تقدمك:</p>

                <!-- Flashcards Mastery Tracker -->
                <div class="flashcards-mastery-banner">
                    <div class="mastery-info">
                        <span>🧠 إتقان بطاقات الاستذكار:</span>
                        <span id="mastery-count">0 من 25 بطاقة متقنة</span>
                    </div>
                    <div class="mastery-track">
                        <div class="mastery-fill" id="mastery-fill"></div>
                    </div>
                </div>'''

content = re.sub(
    r'<!-- TAB 5: FLASHCARDS \(25 KEY TERMS\) -->\s*<section id="tab-cards" class="tab-panel" role="tabpanel">[\s\S]*?<p>اضغط على أي بطاقة[\s\S]*?</p>',
    cards_banner_html,
    content
)

# 4. Replace interactive scripts at the bottom with full UX implementation
new_scripts = '''    <!-- Scripts for Tabs, Flashcards, Quiz, Copy Code, and State Persistence -->
    <script>
        // 1. Tab Switching & Deep Linking
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabPanels = document.querySelectorAll('.tab-panel');

        function activateTab(targetId) {
            tabBtns.forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-selected', 'false');
            });
            tabPanels.forEach(p => p.classList.remove('active'));

            const targetBtn = document.querySelector(`[data-tab="${targetId}"]`);
            const targetPanel = document.getElementById(targetId);
            if (targetBtn && targetPanel) {
                targetBtn.classList.add('active');
                targetBtn.setAttribute('aria-selected', 'true');
                targetPanel.classList.add('active');
            }
        }

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.getAttribute('data-tab');
                activateTab(targetId);
                history.replaceState(null, null, `#${targetId}`);
            });
        });

        // Restore tab from URL hash if provided
        const hash = window.location.hash.slice(1);
        if (hash && document.getElementById(hash)) {
            activateTab(hash);
        }

        // 2. Tactile Floating Copy Code Buttons for all <pre><code> blocks
        document.querySelectorAll('pre').forEach(pre => {
            const btn = document.createElement('button');
            btn.className = 'btn-copy-code';
            btn.type = 'button';
            btn.innerHTML = '📋 نسخ الكود';
            btn.setAttribute('aria-label', 'نسخ الكود إلى الحافظة');

            btn.addEventListener('click', async (e) => {
                e.stopPropagation();
                const codeEl = pre.querySelector('code');
                const rawCode = codeEl ? codeEl.innerText : pre.innerText;
                try {
                    await navigator.clipboard.writeText(rawCode);
                    btn.innerHTML = '✓ تم النسخ!';
                    btn.classList.add('copied');
                    setTimeout(() => {
                        btn.innerHTML = '📋 نسخ الكود';
                        btn.classList.remove('copied');
                    }, 2000);
                } catch (err) {
                    btn.innerHTML = '⚠️ فشل النسخ';
                }
            });
            pre.appendChild(btn);
        });

        // 3. Flashcards Mastery & Persistence
        const flashcards = document.querySelectorAll('.flashcard');
        const masteryStorageKey = 'sir_study_ds_mastered';
        let masteredCards = new Set(JSON.parse(localStorage.getItem(masteryStorageKey) || '[]'));

        function updateMasteryUI() {
            const total = flashcards.length;
            const count = masteredCards.size;
            const pct = Math.round((count / total) * 100);
            const countEl = document.getElementById('mastery-count');
            const fillEl = document.getElementById('mastery-fill');
            if (countEl) countEl.textContent = `${count} من ${total} بطاقة متقنة (${pct}%)`;
            if (fillEl) fillEl.style.width = `${pct}%`;
        }

        flashcards.forEach((card, idx) => {
            if (masteredCards.has(idx)) {
                card.classList.add('mastered');
            }

            // Append mastery control buttons inside card answer area
            const ansArea = card.querySelector('.flashcard-a');
            if (ansArea && !card.querySelector('.mastery-controls')) {
                const controls = document.createElement('div');
                controls.className = 'mastery-controls';
                controls.innerHTML = `
                    <button type="button" class="btn-mastery btn-mastered">✅ أتقنتها تماماً</button>
                    <button type="button" class="btn-mastery btn-review">🔁 تحتاج مراجعة</button>
                `;

                controls.querySelector('.btn-mastered').addEventListener('click', (e) => {
                    e.stopPropagation();
                    masteredCards.add(idx);
                    card.classList.add('mastered');
                    localStorage.setItem(masteryStorageKey, JSON.stringify(Array.from(masteredCards)));
                    updateMasteryUI();
                });

                controls.querySelector('.btn-review').addEventListener('click', (e) => {
                    e.stopPropagation();
                    masteredCards.delete(idx);
                    card.classList.remove('mastered');
                    localStorage.setItem(masteryStorageKey, JSON.stringify(Array.from(masteredCards)));
                    updateMasteryUI();
                });

                ansArea.appendChild(controls);
            }

            function toggleCard() {
                const isFlipped = card.classList.toggle('flipped');
                card.setAttribute('aria-expanded', isFlipped ? 'true' : 'false');
            }

            card.addEventListener('click', toggleCard);
            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleCard();
                }
            });
        });
        updateMasteryUI();

        // 4. Practice Quiz with Score Tracking, Non-blocking Warning & Persistence
        const qItems = document.querySelectorAll('.q-item');
        const quizStorageKey = 'sir_study_ds_quiz_state';
        let quizState = JSON.parse(localStorage.getItem(quizStorageKey) || '{}');

        function updateScoreUI() {
            const total = qItems.length;
            let answered = 0;
            let correctCount = 0;

            qItems.forEach((item, idx) => {
                if (quizState[idx] !== undefined) {
                    answered++;
                    if (quizState[idx].isCorrect) correctCount++;
                }
            });

            const pct = answered > 0 ? Math.round((correctCount / total) * 100) : 0;
            const valEl = document.getElementById('score-val');
            const fillEl = document.getElementById('score-progress-fill');
            if (valEl) valEl.textContent = `${correctCount} / ${total} (${pct}%) — تم حل ${answered}`;
            if (fillEl) fillEl.style.width = `${(answered / total) * 100}%`;
        }

        qItems.forEach((item, qIdx) => {
            const correctIndex = parseInt(item.getAttribute('data-correct'), 10);
            const options = item.querySelectorAll('.option-btn');
            const checkBtn = item.querySelector('.btn-check');
            const exp = item.querySelector('.q-explanation');
            let selectedIndex = null;

            // Create inline warning element
            const warnEl = document.createElement('div');
            warnEl.className = 'inline-warn';
            warnEl.textContent = '⚠️ يرجى تحديد أحد الخيارات أولاً قبل التحقق!';
            checkBtn.insertAdjacentElement('afterend', warnEl);

            options.forEach((opt, idx) => {
                opt.addEventListener('click', () => {
                    if (item.classList.contains('graded')) return;
                    options.forEach(o => o.classList.remove('selected'));
                    selectedIndex = idx;
                    opt.classList.add('selected');
                    warnEl.style.display = 'none';
                });
            });

            function applyGrading(chosenIdx, isCorrect) {
                item.classList.add('graded');
                options.forEach((o, idx) => {
                    o.classList.remove('selected');
                    o.style.pointerEvents = 'none';
                    if (idx === correctIndex) o.classList.add('selected-correct');
                    if (idx === chosenIdx && !isCorrect) o.classList.add('selected-wrong');
                });
                checkBtn.disabled = true;
                checkBtn.innerHTML = '✓ تم التحقق واحتساب الدرجة';
                checkBtn.style.opacity = '0.7';
                exp.classList.add('visible');
            }

            // Restore state if saved
            if (quizState[qIdx] !== undefined) {
                applyGrading(quizState[qIdx].chosen, quizState[qIdx].isCorrect);
            }

            checkBtn.addEventListener('click', () => {
                if (item.classList.contains('graded')) return;
                if (selectedIndex === null) {
                    warnEl.style.display = 'block';
                    return;
                }

                const isCorrect = (selectedIndex === correctIndex);
                quizState[qIdx] = { chosen: selectedIndex, isCorrect };
                localStorage.setItem(quizStorageKey, JSON.stringify(quizState));

                applyGrading(selectedIndex, isCorrect);
                updateScoreUI();
            });
        });

        // Reset Quiz Handler
        const resetBtn = document.getElementById('btn-reset-quiz');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                if (!confirm('هل تريد مسح نتيجة الاختبار وبدء المحاولة من جديد؟')) return;
                localStorage.removeItem(quizStorageKey);
                quizState = {};
                qItems.forEach(item => {
                    item.classList.remove('graded');
                    const options = item.querySelectorAll('.option-btn');
                    options.forEach(o => {
                        o.classList.remove('selected', 'selected-correct', 'selected-wrong');
                        o.style.pointerEvents = 'auto';
                    });
                    const checkBtn = item.querySelector('.btn-check');
                    checkBtn.disabled = false;
                    checkBtn.innerHTML = 'تحقق من الإجابة';
                    checkBtn.style.opacity = '1';
                    const exp = item.querySelector('.q-explanation');
                    if (exp) exp.classList.remove('visible');
                    const warn = item.querySelector('.inline-warn');
                    if (warn) warn.style.display = 'none';
                });
                updateScoreUI();
            });
        }
        updateScoreUI();

        // 5. Live Countdown to Exam (TODAY 08/11/2026 11:30 AM Cairo Time)
        const examDate = new Date('2026-11-08T11:30:00+02:00').getTime();
        const timerElem = document.getElementById('exam-timer');

        function updateTimer() {
            const now = new Date().getTime();
            const dist = examDate - now;

            if (dist <= 0) {
                if (timerElem) timerElem.textContent = 'الامتحان جارٍ الآن أو انتهى!';
                return;
            }

            const hours = Math.floor(dist / (1000 * 60 * 60));
            const minutes = Math.floor((dist % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((dist % (1000 * 60)) / 1000);

            if (timerElem) timerElem.textContent = `${hours}h ${minutes}m ${seconds}s`;
        }

        setInterval(updateTimer, 1000);
        updateTimer();
    </script>
</body>
</html>'''

content = re.sub(
    r'<!-- Scripts for Tabs, Flashcards, Quiz, and Live Countdown -->[\s\S]*?</body>\s*</html>',
    new_scripts,
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated data-structures.html with complete UX mastery and interactive tracking!')
