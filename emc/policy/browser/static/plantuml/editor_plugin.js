(function() { tinymce.PluginManager.requireLangPack('plantuml'); tinymce.create('tinymce.plugins.Plantuml', { init: function(ed, url) { ed.addCommand('mcePlantuml', function() { ed.windowManager.open({ file: url + '/dialog.htm', width: 480 + parseInt(ed.getLang('plantuml.delta_width', 0)), height: 360 + parseInt(ed.getLang('plantuml.delta_height', 0)), inline: 1 }, { plugin_url: url, some_custom_arg: 'custom arg' }) }); ed.addButton('plantuml', { title: 'plantuml.desc', cmd: 'mcePlantuml', image: url + '/img/uml.png' }); ed.onNodeChange.add(function(ed, cm, n) { cm.setActive('plantuml', n.nodeName == 'IMG') }) }, createControl: function(n, cm) { return null }, getInfo: function() { return { longname: 'Insert Code plugin', author: 'Plantuml.com', authorurl: 'http://plantuml.sourceforge.net/', infourl: 'http://plantuml.sourceforge.net/tinymce.html', version: "1.0"} } }); tinymce.PluginManager.add('plantuml', tinymce.plugins.Plantuml) })();