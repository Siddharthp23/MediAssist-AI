import { useState } from "react";
import { generateSummary, generatePlan } from "../services/api";

export default function HealthcareForm() {
  const [input, setInput] = useState("");
  const [summary, setSummary] = useState("");
  const [plan, setPlan] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummary = async () => {
    if (!input) return alert("Please enter input");

    setLoading(true);
    setSummary("");
    try {
      const res = await generateSummary(input);
      setSummary(res.summary);
    } catch (err) {
      setSummary("Error generating summary");
    }
    setLoading(false);
  };

  const handlePlan = async () => {
    if (!input) return alert("Please enter input");

    setLoading(true);
    setPlan("");
    try {
      const res = await generatePlan(input);
      setPlan(res.final_plan);
    } catch (err) {
      setPlan("Error generating plan");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🏥 MediAssist AI</h1>

      {/* Input */}
      <textarea
        placeholder="Enter patient symptoms / diagnosis / goal..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        rows={5}
      />

      {/* Buttons */}
      <div className="button-group">
        <button onClick={handleSummary}>
          Generate Patient Summary
        </button>

        <button onClick={handlePlan}>
          Generate Treatment Plan
        </button>
      </div>

      {/* Loading */}
      {loading && <p>Processing...</p>}

      {/* Output */}
      <div className="output">
        {summary && (
          <>
            <h2>📄 Patient Summary</h2>
            <pre>{summary}</pre>
          </>
        )}

        {plan && (
          <>
            <h2>📋 Treatment Plan</h2>
            <pre>{plan}</pre>
          </>
        )}
      </div>
    </div>
  );
}