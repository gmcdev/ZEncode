﻿package com.ff0000.utils.zencode {    import flash.display.MovieClip;	import flash.events.MouseEvent;	    import flash.desktop.NativeProcess;    import flash.desktop.NativeProcessStartupInfo;    import flash.events.Event;    import flash.events.ProgressEvent;    import flash.events.IOErrorEvent;    import flash.events.NativeProcessExitEvent;    import flash.filesystem.File;	import com.greensock.TweenLite;		public class ZEncode extends MovieClip{		// process utilities		private var confirmProcess:NativeProcess;		private var installFlag:Boolean;		private var installProcess:NativeProcess;				// on stage		public var installFFMPEG:MovieClip;		public var inputVideo:MovieClip;				// constructor code		public function ZEncode() {			addEventListener( Event.ADDED_TO_STAGE, handleAddedToStage );			installFFMPEG.alpha = 0;			inputVideo.alpha = 0;		}				// handle added to stage		private function handleAddedToStage( $_e:Event ):void {			removeEventListener( Event.ADDED_TO_STAGE, handleAddedToStage );			            if( NativeProcess.isSupported ) {                confirmFFMPEGInstall();            }            else {                trace("NativeProcess not supported.");            }		}								// confirm ffmpeg install		private function confirmFFMPEGInstall():void {			trace( this, 'confirmFFMPEGInstall()' );			installFlag = false;			var nativeProcessStartupInfo:NativeProcessStartupInfo = new NativeProcessStartupInfo();			var file:File = File.applicationDirectory.resolvePath( '/usr/bin/python' );			nativeProcessStartupInfo.executable = file;			var processArgs:Vector.<String> = new Vector.<String>();			processArgs[0] = File.applicationDirectory.resolvePath( 'confirm_ffmpeg.py' ).nativePath;			nativeProcessStartupInfo.arguments = processArgs;						confirmProcess = new NativeProcess();			confirmProcess.addEventListener( ProgressEvent.STANDARD_OUTPUT_DATA, handleConfirmOutput );			//confirmProcess.addEventListener( ProgressEvent.STANDARD_OUTPUT_DATA, handleConfirmError );			//confirmProcess.addEventListener( NativeProcessExitEvent.EXIT, handleConfirmComplete );			confirmProcess.start( nativeProcessStartupInfo );		}		private function handleConfirmOutput( $_e:ProgressEvent ):void {			var _result:String = String( confirmProcess.standardOutput.readUTFBytes( confirmProcess.standardOutput.bytesAvailable ));			//trace( 'STDOUT ' + confirmProcess.standardOutput.readUTFBytes( confirmProcess.standardOutput.bytesAvailable ) );			var _status:Array = _result.match( /No\ssuch\sfile\sor\sdirectory/ );			trace( 'CONFIRM FFMPEG RESULT: '+_status );			confirmProcess.exit();			if( _status.length > 0 )				doInstallFFMPEG();			else initUI();		}		// init UI		private function initUI():void {			trace( this, 'initUI()' );			TweenLite.to( inputVideo, 0.3, { alpha: 1 });			inputVideo.browse.addEventListener( MouseEvent.CLICK, handleBrowseFileRequest );			inputVideo.encode.addEventListener( MouseEvent.CLICK, handleEncodeRequest );		}		// handle browse file request		private function handleBrowseFileRequest( $_e:MouseEvent ):void {			trace( 'handle browse' );		}		// handle encode request		private function handleEncodeRequest( $_e:MouseEvent ):void {			trace( 'handle encode' );		}										// -- install ffmpeg 		private function doInstallFFMPEG():void {			trace( this, 'installFFMPEG()' );			TweenLite.to( installFFMPEG, 0.3, { alpha: 1 });						var nativeProcessStartupInfo:NativeProcessStartupInfo = new NativeProcessStartupInfo();			var file:File = File.applicationDirectory.resolvePath( '/usr/bin/python' );			nativeProcessStartupInfo.executable = file;						var processArgs:Vector.<String> = new Vector.<String>();			processArgs[0] = File.applicationDirectory.resolvePath( 'install_ffmpeg.py' ).nativePath;			nativeProcessStartupInfo.arguments = processArgs;						installProcess = new NativeProcess();			installProcess.addEventListener( ProgressEvent.STANDARD_OUTPUT_DATA, onOutputData );			installProcess.addEventListener( ProgressEvent.STANDARD_ERROR_DATA, onErrorData );			installProcess.addEventListener( NativeProcessExitEvent.EXIT, handleProcessComplete );			installProcess.start( nativeProcessStartupInfo );		}		public function onOutputData(event:ProgressEvent):void {			var _output:String = String( installProcess.standardOutput.readUTFBytes( installProcess.standardOutput.bytesAvailable ));			//trace( 'STDOUT: ' + process.standardOutput.readUTFBytes( process.standardOutput.bytesAvailable ) );			var _status:Array = _output.match( /toAS3:.*/ );			if( _status != null )				installFFMPEG.outputTf.text = _status[0].substr( 6 ) + '\n' + installFFMPEG.outputTf.text;		}		public function onErrorData(event:ProgressEvent):void {			//var _output:String = String( process.standardOutput.readUTFBytes( process.standardOutput.bytesAvailable ));			//trace( 'STDERR: ' + process.standardOutput.readUTFBytes( process.standardOutput.bytesAvailable ) );			//var _status:Array = _output.match( /toAS3:.*/ );			//if( _status.length > 0 )				//installFFMPEG.outputTf.text = _status[0] + '\n' + installFFMPEG.outputTf.text;		}		private function handleProcessComplete( $_e:NativeProcessExitEvent ):void {			trace( " - PROCESS COMPLETE: ", $_e.exitCode );			installProcess.removeEventListener( ProgressEvent.STANDARD_OUTPUT_DATA, onOutputData );			installProcess.removeEventListener( ProgressEvent.STANDARD_ERROR_DATA, onErrorData );			installProcess.removeEventListener( NativeProcessExitEvent.EXIT, handleProcessComplete );			TweenLite.to( installFFMPEG, 0.3, { alpha: 0 });			initUI();		}			}	}