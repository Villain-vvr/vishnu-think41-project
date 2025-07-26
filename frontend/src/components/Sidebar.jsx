import React from "react";
import { useChat } from "../context/ChatContext";

const Sidebar = () => {
  console.log("✅ Sidebar rendered");

  return (
    <div className="w-1/4 bg-gray-100 p-4">
      <h2 className="text-lg font-bold mb-2">Sidebar</h2>
    </div>
  );
};

export default Sidebar;



