from create import image as img_module
from create import text

def temp1() :
    overlay_image = img_module.TextOverlayImage()
    overlay_image.add_box(0, 0, 1200, 1200, (0, 0, 255))
    overlay_image.add_box(1200, 0, 800, 1200, (255, 230, 0))
    overlay_image.add_box(0, 1200, 400, 800, (255, 230, 0))
    overlay_image.add_box(400, 1200, 1600, 800, (255, 100, 0))
    overlay_image.add_box(1200-20, 0, 40, 1200, (0, 0, 0))
    overlay_image.add_box(0, 1200-20, 2000, 40, (0, 0, 0))
    overlay_image.add_box(400-20, 1200, 40, 800, (0, 0, 0))
    overlay_image.add_box(150, 150, 1700, 300, (0, 0, 0))
    overlay_image.add_box(150+20, 150+20, 1700-40, 300-40, (255, 255, 255))
    overlay_image.add_text_box("청소년을 위한 풀 파워 공연", 200, 220, (0, 0, 0), (255, 255, 255), font_size=140)
    overlay_image.add_box(150, 600, 500, 1250, (0, 0, 0))
    overlay_image.add_box(150+20, 600+20, 500-40, 1250-40, (255, 255, 255))
    overlay_image.add_box(800, 600, 1050, 1250, (0, 0, 0))
    overlay_image.add_box(800+20, 600+20, 1050-40, 1250-40, (255, 255, 255))
    overlay_image.add_text_box("공연 시간", 200, 650, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("      A      ", 200, 900, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("      B      ", 200, 1200, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("      C      ", 200, 1500, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("공연 내용", 1100, 650, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("      A      ", 1100, 900, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("      B      ", 1100, 1200, (0, 0, 0), (255, 255, 255), font_size=100)
    overlay_image.add_text_box("      C      ", 1100, 1500, (0, 0, 0), (255, 255, 255), font_size=100)
    return overlay_image

def temp2() :
    overlay_image = img_module.TextOverlayImage()
    overlay_image.add_box(0, 0, 2000, 2000, (68, 138, 166))
    
    overlay_image.add_box(150, 150, 1700, 75, (37, 50, 89))
    overlay_image.add_box(150, 2000-150-75, 1700, 75, (37, 50, 89))
    overlay_image.add_box(150, 150, 75, 600, (37, 50, 89))
    overlay_image.add_box(150, 2000-600-150, 75, 600, (37, 50, 89))
    overlay_image.add_box(2000-150-75, 150, 75, 600, (37, 50, 89))
    overlay_image.add_box(2000-150-75, 2000-600-150, 75, 600, (37, 50, 89))
    
    overlay_image.add_text_box("Card News", 400-50, 400, (255, 255, 255), (68, 138, 166), font_path = "NanumGothicBold.ttf", font_size=250)
    overlay_image.add_text_box("Design", 500, 800, (255, 255, 255), (68, 138, 166), font_path = "NanumGothicBold.ttf", font_size=300)
    overlay_image.add_text_box("TIP", 700, 1200, (255, 255, 255), (68, 138, 166), font_path = "NanumGothicBold.ttf", font_size=400)
    return overlay_image

    
def temp3() :
    overlay_image = img_module.TextOverlayImage()
    overlay_image.add_box(0, 0, 2000, 2000, (244, 241, 234))
    
    overlay_image.add_box(0, 100, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 200, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 300, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 400, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 500, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 600, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 700, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 800, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 900, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1000, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1100, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1200, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1300, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1400, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1500, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1600, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1700, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1800, 2000, 4, (227, 226, 222))
    overlay_image.add_box(0, 1900, 2000, 4, (227, 226, 222))
    
    overlay_image.add_box(0, 0, 2000, 150, (38, 76, 1))
    overlay_image.add_box(0, 0, 150, 2000, (38, 76, 1))
    overlay_image.add_box(0, 2000-150, 2000, 150, (38, 76, 1))
    overlay_image.add_box(2000-150, 0, 150, 2000, (38, 76, 1))

    overlay_image.add_circle(150, 150, 250, (38, 76, 1))
    overlay_image.add_circle(2000-150, 150, 250, (38, 76, 1))
    overlay_image.add_circle(150, 2000-150, 250, (38, 76, 1))
    overlay_image.add_circle(2000-150, 2000-150, 250, (38, 76, 1))
    
    overlay_image.add_box(0, 0, 2000, 100, (125, 178, 72))
    overlay_image.add_box(0, 0, 100, 2000, (125, 178, 72))
    overlay_image.add_box(0, 2000-100, 2000, 125, (125, 178, 72))
    overlay_image.add_box(2000-100, 0, 100, 2000, (125, 178, 72))

    overlay_image.add_circle(150, 150, 200, (125, 178, 72))
    overlay_image.add_circle(2000-150, 150, 200, (125, 178, 72))
    overlay_image.add_circle(150, 2000-150, 200, (125, 178, 72))
    overlay_image.add_circle(2000-150, 2000-150, 200, (125, 178, 72))
    
    overlay_image.add_text_box("Card News", 400-50, 400, (125, 178, 72), (244, 241, 234), font_path = "NanumGothicBold.ttf", font_size=250)
    overlay_image.add_text_box("Design", 500+20, 800, (38, 76, 1), (244, 241, 234), font_path = "NanumGothicBold.ttf", font_size=300)
    overlay_image.add_text_box("어떻게 해야 잘 살 수 있을까", 400, 1400, (38, 76, 1), (244, 241, 234), font_path = "NanumGothicBold.ttf", font_size=100)
    return overlay_image


def temp4() :
    overlay_image = img_module.TextOverlayImage()
    overlay_image.add_box(0, 0, 2000, 2000, (68, 92, 166))
    
    overlay_image.add_box(150-5, 400-5, 1700+10, 1200+10, (7, 28, 89))
    overlay_image.add_box(150, 400, 1700, 1200, (169, 181, 217))
    overlay_image.add_box(150+50-5, 400-50-5, 1700-100+10, 1200+10, (7, 28, 89))
    overlay_image.add_box(150+50, 400-50, 1700-100, 1200, (169, 181, 217))
    overlay_image.add_box(150+100-5, 400-100-5, 1700-200+10, 1200+10, (7, 28, 89))
    overlay_image.add_box(150+100, 400-100, 1700-200, 1200, (169, 181, 217))
    
    overlay_image.add_box(150-5, 0, 1700+10, 50+5, (7, 28, 89))
    overlay_image.add_box(150, 0, 1700, 50, (169, 181, 217))
    overlay_image.add_box(150+50-5, 0, 1700-100+10, 100+5, (7, 28, 89))
    overlay_image.add_box(150+50, 0, 1700-100, 100, (169, 181, 217))
    overlay_image.add_box(150+100-5, 0, 1700-200+10, 150+5, (7, 28, 89))
    overlay_image.add_box(150+100, 0, 1700-200, 150, (169, 181, 217))
    
    overlay_image.add_circle(400, 450, 50, (7, 28, 89))
    overlay_image.add_circle(1600, 450, 50, (7, 28, 89))
    overlay_image.add_circle(400, 0, 50, (7, 28, 89))
    overlay_image.add_circle(1600, 0, 50, (7, 28, 89))
    
    overlay_image.add_box(400-25, 0, 50, 450, (151, 123, 116))
    overlay_image.add_box(1600-25, 0, 50, 450, (151, 123, 116))
    
    overlay_image.add_text_box("Card News", 400-50, 500, (0, 0, 0), (169, 181, 217), font_path = "NanumGothicBold.ttf", font_size=250)
    overlay_image.add_text_box("Design", 500+20, 800, (242, 89, 34), (169, 181, 217), font_path = "NanumGothicBold.ttf", font_size=300)
    overlay_image.add_text_box("인포그래픽 AI 생성 위원회", 400, 1800, (255, 255, 255), (68, 92, 166), font_path = "NanumGothicBold.ttf", font_size=100)
    
    return overlay_image