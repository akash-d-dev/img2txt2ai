# import keyboard
# from tools.processAiReq import CallAi
# from tools.process_txt_file import TxtFile
# from tools.process_txt import TxtScreenshot
# from tools.process_txt_file import TxtFile
# from tools.processEvents import Events
# import time


# class Events:
#     # def listen():
#     #     Events.startApp()
#     #     Events.stopApp()
#     #     Events.clearQna()
#     #     Events.createAns()

#     def startApp():
#         while True:
#             print("Starting app")
#             break

#     def stopApp():
#         print("Stopping app")

#     def createQna():
#         keyboard.add_hotkey("right ctrl+0", Events.createQnaHandler)

#     def createQnaHandler():
#         text = TxtScreenshot.getTxtFromClipboard()
#         formatted_text = TxtScreenshot.formatTxt(text)
#         TxtFile.add_q_to_file(formatted_text)

#     def clearQna():
#         keyboard.add_hotkey("right ctrl+9", Events.clearQnaHandler)

#     def clearQnaHandler():
#         with open("temp/qna.txt", "w") as file:
#             file.write("")
#             print("QnA cleared")

#     def createAns():
#         keyboard.add_hotkey("right ctrl+1", Events.createAnsHandler)

#     def createAnsHandler():
#         qna_doc = None
#         while qna_doc is None:
#             qna_doc = CallAi.openAi()
#             time.sleep(55)  # Wait for 1 second before checking again
#         TxtFile.add_a_to_file(qna_doc)

#     def clearAns():
#         keyboard.add_hotkey("right ctrl+8", Events.clearAnsHandler)

#     def clearAnsHandler():
#         with open("temp/ans.txt", "w") as file:
#             file.write("")
#             print("Ans cleared")
