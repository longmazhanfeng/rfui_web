'use strict';

var fs = require('fs');

var $ = require('jquery'), BpmnModeler = require('bpmn-js/lib/Modeler');

var propertiesPanelModule = require('bpmn-js-properties-panel'), propertiesProviderModule = require('bpmn-js-properties-panel/lib/provider/camunda'), camundaModdleDescriptor = require('camunda-bpmn-moddle/resources/camunda'), cliModule = require('bpmn-js-cli');

var container = $('#js-drop-zone');

var canvas = $('#js-canvas');

var bpmnModeler = new BpmnModeler({
	container : canvas,
//	propertiesPanel : {
//		parent : '#js-properties-panel'
//	},
	// propertiesPanelModule, propertiesProviderModule,
	additionalModules : [ cliModule ],
//	moddleExtensions : {
//		camunda : camundaModdleDescriptor
//	},
	cli : {
		bindTo : 'cli'
	}
});

var newDiagramXML = bpmn_dict["bpmn_xml"];

function createNewDiagram() {
	openDiagram(newDiagramXML);
}

function openDiagram(xml) {

	bpmnModeler.importXML(xml, function(err) {

		if (err) {
			container.removeClass('with-diagram').addClass('with-error');

			container.find('.error pre').text(err.message);

			console.error(err);
		} else {
			container.removeClass('with-error').addClass('with-diagram');
		}

	});
}

function saveSVG(done) {
	bpmnModeler.saveSVG(done);
}

function saveDiagram(done) {

	bpmnModeler.saveXML({
		format : true
	}, function(err, xml) {
		done(err, xml);
	});
}

function registerFileDrop(container, callback) {

	function handleFileSelect(e) {
		e.stopPropagation();
		e.preventDefault();

		var files = e.dataTransfer.files;

		var file = files[0];

		var reader = new FileReader();

		reader.onload = function(e) {

			var xml = e.target.result;

			callback(xml);
		};

		reader.readAsText(file);
	}

	function handleDragOver(e) {
		e.stopPropagation();
		e.preventDefault();

		e.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
	}

	container.get(0).addEventListener('dragover', handleDragOver, false);
	container.get(0).addEventListener('drop', handleFileSelect, false);
}

var url = "savejson/";
function autoSaveBPMN(xml) {
	$.ajax({
		"type" : "POST",
		"url" : url,
		"contentType" : "application/json; charset=utf-8",
		"data" : JSON.stringify({
			"xml" : xml
		}),
		"dataType" : "json",
		"beforeSend" : function(xhr, settings) {
			// console.log("Before Send");
			$.ajaxSettings.beforeSend(xhr, settings);
		},
		"success" : function(result) {
			// console.log(result);
		}
	});

}

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = $.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie
						.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

$
		.ajaxSetup({
			beforeSend : function(xhr, settings) {
				if (!(/^http:.*/.test(settings.url) || /^https:.*/
						.test(settings.url))) {
					xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
				}
			}
		});
// //// file drag / drop ///////////////////////

// check file api availability
if (!window.FileList || !window.FileReader) {
	window
			.alert('Looks like you use an older browser that does not support drag and drop. '
					+ 'Try using Chrome, Firefox or the Internet Explorer > 10.');
} else {
	registerFileDrop(container, openDiagram);
}

// bootstrap diagram functions

$(document)
		.on(
				'ready',
				function() {
					
					// if the number of local files is out of 500, throw a error message 
					if(bpmn_dict["MaxError"] != undefined) {
						alert(bpmn_dict["MaxError"]);
					}
					
					// remove drop and create step
					// $('#js-create-diagram').click(function(e) {
					// e.stopPropagation();
					// e.preventDefault();
					//
					// createNewDiagram();
					// });
					// show immediately
					createNewDiagram();
					// add undo function
					$('#js-undo').click(function(e) {
						cli.undo();
					});
					var downloadLink = $('#js-download-diagram');
					var downloadSvgLink = $('#js-download-svg');

//					$('.buttons a').click(function(e) {
//						console.log($(this).is('.active'));
//						if (!$(this).is('.active')) {
//							e.preventDefault();
//							e.stopPropagation();
//						}
//					});

					function setEncoded(link, name, data) {
						var encodedData = encodeURIComponent(data);
						if (data) {
							link
									.addClass('active')
									.attr(
											{
												'href' : 'data:application/bpmn20-xml;charset=UTF-8,'
														+ encodedData,
												'download' : name
											});
						} else {
							link.removeClass('active');
						}
					}

					saveSVG(function(err, svg) {
						setEncoded(downloadSvgLink, 'diagram.svg',
								err ? null : svg);
					});
					// load bpmn xml resource need more time
					$(function() {
						setTimeout(function(){
							saveDiagram(function(err, xml) {
								setEncoded(downloadLink, 'diagram.bpmn', err ? null
										: xml);
							});
						})
					}, 800);					
					
					var debounce = require('lodash/function/debounce');

					var exportArtifacts = debounce(function() {
						saveSVG(function(err, svg) {
							setEncoded(downloadSvgLink, 'diagram.svg',
									err ? null : svg);
						});

						saveDiagram(function(err, xml) {
							setEncoded(downloadLink, 'diagram.bpmn', err ? null
									: xml);
							autoSaveBPMN(xml);
						});
					}, 500);

					// listen bpmn commandStack.changed event
					bpmnModeler.on('commandStack.changed', exportArtifacts);
				});
