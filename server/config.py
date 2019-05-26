def server_init(app):
    app.config['SCAN_STATUS_START'] = '准备扫描资源'
    app.config['SCAN_STATUS_PORTSCAN'] = '端口扫描'
    app.config['SCAN_STATUS_VULNSCAN'] = '脆弱性信息收集'
    app.config['SCAN_STATUS_FIN'] = '清理扫描缓存'
