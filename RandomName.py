import random

first_name_array = [
    "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈",  "蒋", "沈", "韩", "杨", "朱", "秦", "许", "何", "吕", "施",
    '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
    '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
    '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
    '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
    '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
    '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
    '熊', '纪', '舒', '屈', '项', '祝', '董', '梁'
]
last_name_array = [
    "伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文","明浩", "光", "超", "军", "达",
    "一", "乙", "二", "十", "丁", "厂", "七", "卜", "人", "入", "八", "九", "几", "儿", "了", "力", "乃", "刀", "又", "三",
    "于", "干", "亏", "士", "工", "土", "才", "寸", "下", "大", "丈", "与", "万", "上", "小", "口", "巾", "山", "千", "乞",
    "川", "亿", "个", "勺", "久", "凡", "及", "夕", "丸", "么", "广", "亡", "门", "义", "之", "尸", "弓", "己", "已", "子",
    "卫", "也", "女", "飞", "刃", "习", "叉", "马", "乡", "丰", "王", "井", "开", "夫", "天", "无", "元", "专", "云", "扎",
    "艺", "木", "五", "支", "厅", "不", "太", "犬", "区", "历", "尤", "友", "匹", "车", "巨", "牙", "屯", "比", "互", "切",
    "瓦", "止", "少", "日", "中", "冈", "贝", "内", "水", "见", "午", "牛", "手", "毛", "气", "升", "长", "仁", "什", "片",
    "仆", "化", "仇", "币", "仍", "仅", "斤", "爪", "反", "介", "父", "从", "今", "凶", "分", "乏", "公", "仓", "月", "氏",
    "勿", "欠", "风", "丹", "匀", "乌", "凤", "勾", "文", "六", "方", "火", "为", "斗", "忆", "订", "计", "户", "认", "心",
    "尺", "引", "丑", "巴", "孔", "队", "办", "以", "允", "予", "劝", "双", "书", "幻", "玉", "刊", "示", "末", "未", "击",
    "打", "巧", "正", "扑", "扒", "功", "扔", "去", "甘", "世", "古", "节", "本", "术", "可", "丙", "左", "厉", "右", "石",
    "布", "龙", "平", "灭", "轧", "东", "卡", "北", "占", "业", "旧", "帅", "归", "且", "旦", "目", "叶", "甲", "申", "叮",
    "电", "号", "田", "由", "史", "只", "央", "兄", "叼", "叫", "另", "叨", "叹", "四", "生", "失", "禾", "丘", "付", "仗",
    "代", "仙", "们", "仪", "白", "仔", "他", "斥", "瓜", "乎", "丛", "令", "用", "甩", "印", "乐", "句", "匆", "册", "犯",
    "外", "处", "冬", "鸟", "务", "包", "饥", "主", "市", "立", "闪", "兰", "半", "汁", "汇", "头", "汉", "宁", "穴", "它",
    "讨", "写", "让", "礼", "训", "必", "议", "讯", "记", "永", "司", "尼", "民", "出", "辽", "奶", "奴", "加", "召", "皮",
    "边", "发", "孕", "圣", "对", "台", "矛", "纠", "母", "幼", "丝", "式", "刑", "动", "扛", "寺", "吉", "扣", "考", "托",
    "老", "执", "巩", "圾", "扩", "扫", "地", "扬", "场", "耳", "共", "芒", "亚", "芝", "朽", "朴", "机", "权", "过", "臣",
    "再", "协", "西", "压", "厌", "在", "有", "百", "存", "而", "页", "匠", "夸", "夺", "灰", "达", "列", "死", "成", "夹",
    "轨", "邪", "划", "迈", "毕", "至", "此", "贞", "师", "尘", "尖", "劣", "光", "当", "早", "吐", "吓", "虫", "曲", "团",
    "同", "吊", "吃", "因", "吸", "吗", "屿", "帆", "岁", "回", "岂", "刚", "则", "肉", "网", "年", "朱", "先", "丢", "舌",
    "竹", "迁", "乔", "伟", "传", "乒", "乓", "休", "伍", "伏", "优", "伐", "延", "件", "任", "伤", "价", "份", "华", "仰",
    "仿", "伙", "伪", "自", "血", "向", "似", "后", "行", "舟", "全", "会", "杀", "合", "兆", "企", "众", "爷", "伞", "创",
    "肌", "朵", "杂", "危", "旬", "旨", "负", "各", "名", "多", "争", "色", "壮", "冲", "冰", "庄", "庆", "亦", "刘", "齐",
    "交", "次", "衣", "产", "决", "充", "妄", "闭", "问", "闯", "羊", "并", "关", "米", "灯", "州", "汗", "污", "江", "池",
    "汤", "忙", "兴", "宇", "守", "宅", "字", "安", "讲", "军", "许", "论", "农", "讽", "设", "访", "寻", "那", "迅", "尽",
    "导", "异", "孙", "阵", "阳", "收", "阶", "阴", "防", "奸", "如", "妇", "好", "她", "妈", "戏", "羽", "观", "欢", "买",
    "红", "纤", "级", "约", "纪", "驰", "巡", "寿", "弄", "麦", "形", "进", "戒", "吞", "远", "违", "运", "扶", "抚", "坛",
    "技", "坏", "扰", "拒", "找", "批", "扯", "址", "走", "抄", "坝", "贡", "攻", "赤", "折", "抓", "扮", "抢", "孝", "均",
    "抛", "投", "坟", "抗", "坑", "坊", "抖", "护", "壳", "志", "扭", "块", "声", "把", "报", "却", "劫", "芽", "花", "芹",
    "芬", "苍", "芳", "严", "芦", "劳", "克", "苏", "杆", "杠", "杜", "材", "村", "杏", "极", "李", "杨", "求", "更", "束",
    "豆", "两", "丽", "医", "辰", "励", "否", "还", "歼", "来", "连", "步", "坚", "旱", "盯", "呈", "时", "吴", "助", "县",
    "里", "呆", "园", "旷", "围", "足", "邮", "男", "困", "吵", "串", "员", "听", "吩", "吹", "呜", "吧", "吼",
    "别", "岗", "帐", "财", "针", "钉", "告", "我", "乱", "利", "秃", "秀", "私", "每", "兵", "估", "体", "何", "但", "伸",
    "作", "伯", "伶", "佣", "低", "你", "住", "位", "伴", "身", "皂", "佛", "近", "彻", "役", "返", "余", "希", "坐", "谷",
    "妥", "含", "邻", "岔", "肝", "肚", "肠", "龟", "免", "狂", "犹", "角", "删", "条", "卵", "岛", "迎", "饭", "饮", "系",
    "言", "冻", "状", "亩", "况", "床", "库", "疗", "应", "冷", "这", "序", "辛", "弃", "冶", "忘", "闲", "间", "闷", "判",
    "灶", "灿", "弟", "汪", "沙", "汽", "沃", "泛", "沟", "没", "沈", "沉", "怀", "忧", "快", "完", "宋", "宏", "牢", "究",
    "穷", "灾", "良", "证", "启", "评", "补", "初", "社", "识", "诉", "诊", "词", "译", "君", "灵", "即", "层", "尿", "尾",
    "迟", "局", "改", "张", "忌", "际", "陆", "阿", "陈", "阻", "附", "妙", "妖", "妨", "努", "忍", "劲", "鸡", "驱", "纯",
    "纱", "纳", "纲", "驳", "纵", "纷", "纸", "纹", "纺", "驴", "纽", "奉", "玩", "环", "武", "青", "责", "现", "表", "规",
    "抹", "拢", "拔", "拣", "担", "坦", "押", "抽", "拐", "拖", "拍", "者", "顶", "拆", "拥", "抵", "拘", "势", "抱", "垃",
    "拉", "拦", "拌", "幸", "招", "坡", "披", "拨", "择", "抬", "其", "取", "苦", "若", "茂", "苹", "苗", "英", "范", "直",
    "茄", "茎", "茅", "林", "枝", "杯", "柜", "析", "板", "松", "枪", "构", "杰", "述", "枕", "丧", "或", "画", "卧", "事",
    "刺", "枣", "雨", "卖", "矿", "码", "厕", "奔", "奇", "奋", "态", "欧", "垄", "妻", "轰", "顷", "转", "斩", "轮", "软",
    "到", "非", "叔", "肯", "齿", "些", "虎", "虏", "肾", "贤", "尚", "旺", "具", "果", "味", "昆", "国", "昌", "畅", "明",
    "易", "昂", "典", "固", "忠", "咐", "呼", "鸣", "咏", "呢", "岸", "岩", "帖", "罗", "帜", "岭", "凯", "败", "贩", "购",
    "图", "钓", "制", "知", "垂", "牧", "物", "乖", "刮", "秆", "和", "季", "委", "佳", "侍", "供", "使", "例", "版", "侄",
    "侦", "侧", "凭", "侨", "佩", "货", "依", "的", "迫", "质", "欣", "征", "往", "爬", "彼", "径", "所", "舍", "金", "命",
    "斧", "爸", "采", "受", "乳", "贪", "念", "贫", "肤", "肺", "肢", "肿", "胀", "朋", "股", "肥", "服", "胁", "周", "昏",
    "鱼", "兔", "狐", "忽", "狗", "备", "饰", "饱", "饲", "变", "京", "享", "店", "夜", "庙", "府", "底", "剂", "郊", "废",
    "净", "盲", "放", "刻", "育", "闸", "闹", "郑", "券", "卷", "单", "炒", "炊", "炕", "炎", "炉", "沫", "浅", "法", "泄",
    "河", "沾", "泪", "油", "泊", "沿", "泡", "注", "泻", "泳", "泥", "沸", "波", "泼", "泽", "治", "怖", "性", "怕", "怜",
    "怪", "学", "宝", "宗", "定", "宜", "审", "宙", "官", "空", "帘", "实", "试", "郎", "诗", "肩", "房", "诚", "衬", "衫",
    "视", "话", "诞", "询", "该", "详", "建", "肃", "录", "隶", "居", "届", "刷", "屈", "弦", "承", "孟", "孤", "陕", "降",
    "限", "妹", "姑", "姐", "姓", "始", "驾", "参", "艰", "线", "练", "组", "细", "驶", "织", "终", "驻", "驼", "绍", "经",
    "贯", "奏", "春", "帮", "珍", "玻", "毒", "型", "挂", "封", "持", "项", "垮", "挎", "城", "挠", "政", "赴", "赵", "挡",
    "挺", "括", "拴", "拾", "挑", "指", "垫", "挣", "挤", "拼", "挖", "按", "挥", "挪", "某", "甚", "革", "荐", "巷", "带",
    "草", "茧", "茶", "荒", "茫", "荡", "荣", "故", "胡", "南", "药", "标", "枯", "柄", "栋", "相", "查", "柏", "柳", "柱",
    "柿", "栏", "树", "要", "咸", "威", "歪", "研", "砖", "厘", "厚", "砌", "砍", "面", "耐", "耍", "牵", "残", "殃", "轻",
    "鸦", "皆", "背", "战", "点", "临", "览", "竖", "省", "削", "尝", "是", "盼", "眨", "哄", "显", "哑", "冒", "映", "星",
    "昨", "畏", "趴", "胃", "贵", "界", "虹", "虾", "蚁", "思", "蚂", "虽", "品", "咽", "骂", "哗", "咱", "响", "哈", "咬",
    "咳", "哪", "炭", "峡", "罚", "贱", "贴", "骨", "钞", "钟", "钢", "钥", "钩", "卸", "缸", "拜", "看", "矩", "怎", "牲",
    "选", "适", "秒", "香", "种", "秋", "科", "重", "复", "竿", "段", "便", "俩", "贷", "顺", "修", "保", "促", "侮", "俭",
    "俗", "俘", "信", "皇", "泉", "鬼", "侵", "追", "俊", "盾", "待", "律", "很", "须", "叙", "剑", "逃", "食", "盆", "胆",
    "胜", "胞", "胖", "脉", "勉", "狭", "狮", "独", "狡", "狱", "狠", "贸", "怨", "急", "饶", "蚀", "饺", "饼", "弯", "将",
    "奖", "哀", "亭", "亮", "度", "迹", "庭", "疮", "疯", "疫", "疤", "姿", "亲", "音", "帝", "施", "闻", "阀", "阁", "差",
    "养", "美", "姜", "叛", "送", "类", "迷", "前", "首", "逆", "总", "炼", "炸", "炮", "烂", "剃", "洁", "洪", "洒", "浇",
    "浊", "洞", "测", "洗", "活", "派", "洽", "染", "济", "洋", "洲", "浑", "浓", "津", "恒", "恢", "恰", "恼", "恨", "举",
    "觉", "宣", "室", "宫", "宪", "突", "穿", "窃", "客", "冠", "语", "扁", "袄", "祖", "神", "祝", "误", "诱", "说", "诵",
    "垦", "退", "既", "屋", "昼", "费", "陡", "眉", "孩", "除", "险", "院", "娃", "姥", "姨", "姻", "娇", "怒", "架", "贺",
    "盈", "勇", "怠", "柔", "垒", "绑", "绒", "结", "绕", "骄", "绘", "给", "络", "骆", "绝", "绞", "统", "耕", "耗", "艳",
    "泰", "珠", "班", "素", "蚕", "顽", "盏", "匪", "捞", "栽", "捕", "振", "载", "赶", "起", "盐", "捎", "捏", "埋", "捉",
    "捆", "捐", "损", "都", "哲", "逝", "捡", "换", "挽", "热", "恐", "壶", "挨", "耻", "耽", "恭", "莲", "莫", "荷", "获",
    "晋", "恶", "真", "框", "桂", "档", "桐", "株", "桥", "桃", "格", "校", "核", "样", "根", "索", "哥", "速", "逗", "栗",
    "配", "翅", "辱", "唇", "夏", "础", "破", "原", "套", "逐", "烈", "殊", "顾", "轿", "较", "顿", "毙", "致", "柴", "桌",
    "虑", "监", "紧", "党", "晒", "眠", "晓", "鸭", "晃", "晌", "晕", "蚊", "哨", "哭", "恩", "唤", "啊", "唉", "罢", "峰",
    "圆", "贼", "贿", "钱", "钳", "钻", "铁", "铃", "铅", "缺", "氧", "特", "牺", "造", "乘", "敌", "秤", "租", "积", "秧",
    "秩", "称", "秘", "透", "笔", "笑", "笋", "债", "借", "值", "倚", "倾", "倒", "倘", "俱", "倡", "候", "俯", "倍", "倦",
    "健", "臭", "射", "躬", "息", "徒", "徐", "舰", "舱", "般", "航", "途", "拿", "爹", "爱", "颂", "翁", "脆", "脂", "胸",
    "胳", "脏", "胶", "脑", "狸", "狼", "逢", "留", "皱", "饿", "恋", "桨", "浆", "衰", "高", "席", "准", "座", "脊", "症",
    "病", "疾", "疼", "疲", "效", "离", "唐", "资", "凉", "站", "剖", "竞", "部", "旁", "旅", "畜", "阅", "羞", "瓶", "拳",
    "粉", "料", "益", "兼", "烤", "烘", "烦", "烧", "烛", "烟", "递", "涛", "浙", "涝", "酒", "涉", "消", "浩", "海", "涂",
    "浴", "浮", "流", "润", "浪", "浸", "涨", "烫", "涌", "悟", "悄", "悔", "悦", "害", "宽", "家", "宵", "宴", "宾", "窄",
    "容", "宰", "案", "请", "朗", "诸", "读", "扇", "袜", "袖", "袍", "被", "祥", "课", "谁", "调", "冤", "谅", "谈", "谊",
    "剥", "恳", "展", "剧", "屑", "弱", "陵", "陶", "陷", "陪", "娱", "娘", "通", "能", "难", "预", "桑", "绢", "绣", "验",
    "继", "球", "理", "捧", "堵", "描", "域", "掩", "捷", "排", "掉", "堆", "推", "掀", "授", "教", "掏", "掠", "培", "接",
    "控", "探", "据", "掘", "职", "基", "著", "勒", "黄", "萌", "萝", "菌", "菜", "萄", "菊", "萍", "菠", "营", "械", "梦",
    "梢", "梅", "检", "梳", "梯", "桶", "救", "副", "票", "戚", "爽", "聋", "袭", "盛", "雪", "辅", "辆", "虚", "雀", "堂",
    "常", "匙", "晨", "睁", "眯", "眼", "悬", "野", "啦", "晚", "啄", "距", "跃", "略", "蛇", "累", "唱", "患", "唯", "崖",
    "崭", "崇", "圈", "铜", "铲", "银", "甜", "梨", "犁", "移", "笨", "笼", "笛", "符", "第", "敏", "做", "袋", "悠", "偿",
    "偶", "偷", "您", "售", "停", "偏", "假", "得", "衔", "盘", "船", "斜", "盒", "鸽", "悉", "欲", "彩", "领", "脚", "脖",
    "脱", "象", "够", "猜", "猪", "猎", "猫", "猛", "馅", "馆", "凑", "减", "毫", "麻", "痒", "痕", "廊", "康", "庸",
    "鹿", "盗", "章", "竟", "商", "族", "旋", "望", "率", "着", "盖", "粘", "粗", "粒", "断", "剪", "兽", "清", "添", "淋",
    "淹", "渠", "渐", "混", "渔", "淘", "液", "淡", "深", "婆", "梁", "渗", "情", "惜", "惭", "悼", "惧", "惕", "惊", "惨",
    "惯", "寇", "寄", "宿", "窑", "密", "谋", "谎", "祸", "谜", "逮", "敢", "屠", "弹", "随", "蛋", "隆", "隐", "婚", "婶",
    "颈", "绩", "绪", "续", "骑", "绳", "维", "绵", "绸", "绿", "琴", "斑", "替", "款", "堪", "搭", "塔", "越", "趁", "趋",
    "超", "提", "堤", "博", "揭", "喜", "插", "揪", "搜", "煮", "援", "裁", "搁", "搂", "搅", "握", "揉", "斯", "期", "欺",
    "联", "散", "惹", "葬", "葛", "董", "葡", "敬", "葱", "落", "朝", "辜", "葵", "棒", "棋", "植", "森", "椅", "椒", "棵",
    "棍", "棉", "棚", "棕", "惠", "惑", "逼", "厨", "厦", "硬", "确", "雁", "殖", "裂", "雄", "暂", "雅", "辈", "悲", "紫",
    "辉", "敞", "赏", "掌", "晴", "暑", "最", "量", "喷", "晶", "喇", "遇", "喊", "景", "践", "跌", "跑", "遗", "蛙", "蛛",
    "蜓", "喝", "喂", "喘", "喉", "幅", "帽", "赌", "赔", "黑", "铸", "铺", "链", "销", "锁", "锄", "锅", "锈", "锋", "锐",
    "短", "智", "毯", "鹅", "剩", "稍", "程", "稀", "税", "筐", "等", "筑", "策", "筛", "筒", "答", "筋", "筝", "傲", "傅",
    "牌", "堡", "集", "焦", "傍", "储", "奥", "街", "惩", "御", "循", "艇", "舒", "番", "释", "禽", "腊", "脾", "腔", "鲁",
    "猾", "猴", "然", "馋", "装", "蛮", "就", "痛", "童", "阔", "善", "羡", "普", "粪", "尊", "道", "曾", "焰", "港", "湖",
    "渣", "湿", "温", "渴", "滑", "湾", "渡", "游", "滋", "溉", "愤", "慌", "惰", "愧", "愉", "慨", "割", "寒", "富", "窜",
    "窝", "窗", "遍", "裕", "裤", "裙", "谢", "谣", "谦", "属", "屡", "强", "粥", "疏", "隔", "隙", "絮", "嫂", "登", "缎",
    "缓", "编", "骗", "缘", "瑞", "魂", "肆", "摄", "摸", "填", "搏", "塌", "鼓", "摆", "携", "搬", "摇", "搞", "塘", "摊",
    "蒜", "勤", "鹊", "蓝", "墓", "幕", "蓬", "蓄", "蒙", "蒸", "献", "禁", "楚", "想", "槐", "榆", "楼", "概", "赖", "酬",
    "感", "碍", "碑", "碎", "碰", "碗", "碌", "雷", "零", "雾", "雹", "输", "督", "龄", "鉴", "睛", "睡", "睬", "鄙", "愚",
    "暖", "盟", "歇", "暗", "照", "跨", "跳", "跪", "路", "跟", "遣", "蛾", "蜂", "嗓", "置", "罪", "罩", "错", "锡", "锣",
    "锤", "锦", "键", "锯", "矮", "辞", "稠", "愁", "筹", "签", "简", "毁", "舅", "鼠", "催", "傻", "像", "躲", "微", "愈",
    "遥", "腰", "腥", "腹", "腾", "腿", "触", "解", "酱", "痰", "廉", "新", "韵", "意", "粮", "数", "煎", "塑", "慈", "煤",
    "煌", "满", "漠", "源", "滤", "滥", "滔", "溪", "溜", "滚", "滨", "粱", "滩", "慎", "誉", "塞", "谨", "福", "群", "殿",
    "辟", "障", "嫌", "嫁", "叠", "缝", "缠", "静", "碧", "璃", "墙", "撇", "嘉", "摧", "截", "誓", "境", "摘", "摔", "聚",
    "蔽", "慕", "暮", "蔑", "模", "榴", "榜", "榨", "歌", "遭", "酷", "酿", "酸", "磁", "愿", "需", "弊", "裳", "颗", "嗽",
    "蜻", "蜡", "蝇", "蜘", "赚", "锹", "锻", "舞", "稳", "算", "箩", "管", "僚", "鼻", "魄", "貌", "膜", "膊", "膀", "鲜",
    "疑", "馒", "裹", "敲", "豪", "膏", "遮", "腐", "瘦", "辣", "竭", "端", "旗", "精", "歉", "熄", "熔", "漆", "漂", "漫",
    "滴", "演", "漏", "慢", "寨", "赛", "察", "蜜", "谱", "嫩", "翠", "熊", "凳", "骡", "缩", "慧", "撕", "撒", "趣", "趟",
    "撑", "播", "撞", "撤", "增", "聪", "鞋", "蕉", "蔬", "横", "槽", "樱", "橡", "飘", "醋", "醉", "震", "霉", "瞒", "题",
    "暴", "瞎", "影", "踢", "踏", "踩", "踪", "蝶", "蝴", "嘱", "墨", "镇", "靠", "稻", "黎", "稿", "稼", "箱", "箭", "篇",
    "僵", "躺", "僻", "德", "艘", "膝", "膛", "熟", "摩", "颜", "毅", "糊", "遵", "潜", "潮", "懂", "额", "慰", "劈", "操",
    "燕", "薯", "薪", "薄", "颠", "橘", "整", "融", "醒", "餐", "嘴", "蹄", "器", "赠", "默", "镜", "赞", "篮", "邀", "衡",
    "膨", "雕", "磨", "凝", "辨", "辩", "糖", "糕", "燃", "澡", "激", "懒", "壁", "避", "缴", "戴", "擦", "鞠", "藏", "霜",
    "霞", "瞧", "蹈", "螺", "穗", "繁", "辫", "赢", "糟", "糠", "燥", "臂", "翼", "骤", "鞭", "覆", "蹦", "镰", "翻", "鹰",
    "警", "攀", "蹲", "颤", "瓣", "爆", "疆", "壤", "耀", "躁", "嚼", "嚷", "籍", "魔", "灌", "蠢", "霸", "露", "囊", "罐",
    '的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
    '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
    '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
    '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
    '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
    '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
    '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
    '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
    '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
    '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
    '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
    '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
    '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
    '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
    '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
    '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
    '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
    '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
    '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
    '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
    '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
    '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
    '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
    '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
    '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
    '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
    '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
    '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
    '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
    '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
    '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
    '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
    '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
    '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
    '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
    '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
    '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
    '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
    '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
    '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
    '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
    '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
    '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
    '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
    '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
    '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
    '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
    '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
    '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
    '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
    '乾', '坤'
]
"""
array length
"""
first_name_size = first_name_array.__len__()
last_name_size = last_name_array.__len__()


def fullname():
    """
    获取一个随机名，名的长度1或2
    :return:
    """
    first_name = first_name_array[random.randint(0, first_name_size)]
    last_name = ''.join(last_name_array[random.randint(0, last_name_size)] for i in range(random.randint(1, 2)))
    return first_name + last_name


for i in range(0, 10):
    print(fullname())