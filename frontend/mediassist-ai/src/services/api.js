const BASE_URL = "http://backend:8000";

export const generateSummary = async (inputText) => {
  return fetch(`${BASE_URL}/generate-summary`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input_text: inputText }),
  }).then(res => res.json());
};

export const generatePlan = async (inputText) => {
  return fetch(`${BASE_URL}/generate-plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input_text: inputText }),
  }).then(res => res.json());
};