import ContentCopyIcon from "@mui/icons-material/ContentCopy";
import DoneIcon from "@mui/icons-material/Done";
import { IconButton } from "@mui/material";
import { useState } from "react";

const CopyToClipBtn = ({ active, quesFile, ansFile }) => {
  const [copying, setCopying] = useState(false);

  const copyToClipboard = (text) => {
    const textarea = document.createElement("textarea");
    const replacedText = text.replace(/<br>/g, "\n").replace(/&nbsp;/g, " ");
    textarea.textContent = replacedText;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
  };

  const handleCopy = () => {
    setCopying(true);
    setTimeout(() => {
      setCopying(false);
    }, 500);

    let textToCopy = "";

    switch (active) {
      case 0:
        textToCopy = quesFile.qna_prompt;
        break;
      case 1:
        textToCopy = ansFile.ans_gpt;
        break;
      case 2:
        textToCopy = ansFile.ans_gemini;
        break;
      case 3:
        textToCopy = ansFile.ans_gemini_img;
        break;
      case 4:
        textToCopy = quesFile.qna;
        break;
      default:
        textToCopy = "";
    }

    copyToClipboard(textToCopy);
  };

  return (
    <IconButton
      onClick={handleCopy}
      sx={{
        position: "fixed",
        bottom: "70px",
        left: "75%",
        zIndex: "100",
        bgcolor: "#585858",
        p: 2.5,
        mx: 0.5,
        mt: 2,
        width: 30,
        height: 30,
      }}
    >
      {copying ? <DoneIcon /> : <ContentCopyIcon />}
    </IconButton>
  );
};

export default CopyToClipBtn;
