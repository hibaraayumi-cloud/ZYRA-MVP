def get_recommendations(
    revenue,
    cost,
    cash,
    growth
):

    recommendations = []

    if growth < 0:

        recommendations.append(
            "ควรจัดทำกิจกรรมรักษาฐานลูกค้าและเพิ่มการกลับมาซื้อซ้ำ"
        )

    if cash < revenue * 0.3:

        recommendations.append(
            "ควรเพิ่มเงินสดสำรองให้เพียงพอต่อค่าใช้จ่ายในระยะสั้น"
        )

    if revenue < cost:

        recommendations.append(
            "ควรปรับโครงสร้างต้นทุนและทบทวนกลยุทธ์ด้านราคา"
        )

    if len(recommendations) == 0:

        recommendations.append(
            "ธุรกิจอยู่ในเกณฑ์ปกติ ควรติดตามผลอย่างต่อเนื่อง"
        )

    return recommendations
