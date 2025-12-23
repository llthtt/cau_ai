/*********************************************************
 * Bé Cậu – Frontend Controller (HOÀN THIỆN – FIX AUTO RESIZE MIC)
 *********************************************************/

// ================= CORE ELEMENTS =================
const chatBox = document.getElementById("chatBox");
const input = document.getElementById("input"); // textarea
const sendBtn = document.getElementById("sendBtn");
const micBtn = document.getElementById("micBtn");

// ================= STOP SPEAK =================
function stopSpeak() {
  if (window.speechSynthesis) speechSynthesis.cancel();
}

if (input) {
  input.addEventListener("focus", stopSpeak);
  input.addEventListener("keydown", stopSpeak);
}
if (micBtn) {
  micBtn.addEventListener("click", stopSpeak);
}

// ================= AUTO RESIZE INPUT =================
const MAX_HEIGHT = 140;
function resizeInput() {
  input.style.height = "auto";
  input.style.height = Math.min(input.scrollHeight, MAX_HEIGHT) + "px";
}
input.addEventListener("input", resizeInput);
input.addEventListener("focus", resizeInput);

// ================= MIC OVERLAY =================
const micOverlay = document.createElement("div");
micOverlay.textContent = "🎤 Bé Cậu đang nghe…";
micOverlay.style.position = "absolute";
micOverlay.style.bottom = "70px";
micOverlay.style.left = "50%";
micOverlay.style.transform = "translateX(-50%)";
micOverlay.style.fontSize = "13px";
micOverlay.style.opacity = "0.45";
micOverlay.style.pointerEvents = "none";
micOverlay.style.display = "none";
chatBox.parentNode.appendChild(micOverlay);

// ================= TTS SPEED CONTROL (4–8) =================
let userSpeechRate = 6;
const rateBox = document.createElement("div");
rateBox.style.position = "absolute";
rateBox.style.top = "8px";
rateBox.style.right = "8px";
rateBox.style.fontSize = "12px";
rateBox.style.opacity = "0.7";
rateBox.style.zIndex = "10";
rateBox.innerHTML = `
🔊 <select id="ttsRate">
  <option value="4">4</option>
  <option value="5">5</option>
  <option value="6" selected>6</option>
  <option value="7">7</option>
  <option value="8">8</option>
</select>`;
chatBox.parentNode.appendChild(rateBox);
document.getElementById("ttsRate").onchange = e => {
  userSpeechRate = Number(e.target.value);
};

// ================= ADD MESSAGE =================
function addMessage(text, cls) {
  const div = document.createElement("div");
  div.className = `message ${cls}`;
  div.textContent = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
  if (cls === "assistant") speak(text);
}

// ================= SEND CHAT =================
function send() {
  const text = input.value.trim();
  if (!text) return;

  stopSpeak();
  addMessage(text, "user");
  input.value = "";
  resizeInput();

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  })
    .then(r => r.json())
    .then(d => addMessage(d.reply || "❌ Không có phản hồi", "assistant"))
    .catch(() => addMessage("❌ Lỗi kết nối", "assistant"));
}

sendBtn.onclick = send;
input.onkeydown = e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    send();
  }
};

// ================= TEXT TO SPEECH =================
function speak(text) {
  if (!window.speechSynthesis) return;
  stopSpeak();

  const clean = text.replace(/[*_#—]/g, "").trim();
  if (!clean) return;

  const msg = new SpeechSynthesisUtterance(clean);
  msg.lang = "vi-VN";
  let baseRate = clean.length < 40 ? 0.9 : clean.length < 120 ? 1.0 : 1.1;
  const rateMap = {4:0.85,5:0.95,6:1.05,7:1.15,8:1.25};
  msg.rate = baseRate * (rateMap[userSpeechRate] || 1.05);
  speechSynthesis.speak(msg);
}

// ================= MIC ADD-ON A (FIX RESIZE) =================
(function () {
  if (!("webkitSpeechRecognition" in window)) return;

  const rec = new webkitSpeechRecognition();
  rec.lang = "vi-VN";
  rec.continuous = true;
  rec.interimResults = true;

  let silenceTimer = null;
  let lastText = "";

  function resetTimer() {
    clearTimeout(silenceTimer);
    silenceTimer = setTimeout(() => rec.stop(), 2000);
  }

  rec.onstart = () => {
    stopSpeak();
    micOverlay.style.display = "block";
    resetTimer();
  };

  rec.onresult = e => {
    let text = "";
    for (let i = e.resultIndex; i < e.results.length; i++) {
      text += e.results[i][0].transcript;
    }
    lastText = text.trim();
    input.value = lastText;
    resizeInput(); // 🔥 FIX QUAN TRỌNG
    resetTimer();
  };

  rec.onend = () => {
    micOverlay.style.display = "none";
    clearTimeout(silenceTimer);
    if (lastText) send();
  };

  if (micBtn) {
    micBtn.addEventListener("click", () => {
      try { rec.start(); } catch {}
    });
  }
})();
