import React, { useEffect } from "react";
import { useChat } from "../context/ChatContext";

const SidePanel = () => {
  const { sessions, fetchSessions, loadSession, currentSession } = useChat();

  useEffect(() => {
    fetchSessions();
  }, []);

  return (
    <div className="side-panel">
      <h3>Past Conversations</h3>
      <ul>
        {sessions.map((id) => (
          <li
            key={id}
            style={{ fontWeight: id === currentSession ? "bold" : "normal", cursor: "pointer" }}
            onClick={() => loadSession(id)}
          >
            {id}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SidePanel;